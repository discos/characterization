from __future__ import annotations

import json
import logging
import math
from pathlib import Path
from statistics import mean
from typing import Any

import click
from astropy import units as u
from astropy.coordinates import Angle
from astropy.coordinates import EarthLocation
from astropy.io import fits
from prefect import flow
from prefect import get_run_logger
from prefect import task


observatories = {
    "MED": "Medicina Radio Telescope",
    "SRT": "Sardinia Radio Telescope",
    "NOT": "Noto Radio Telescope",
}


@task(description="{observatory} location from Astropy")
def location_from_astropy(observatory: str = "SRT") -> EarthLocation:
    return EarthLocation.of_site(observatory)


@task(description="FITS file produced at {observatory}", persist_result=True)
def observatory_file(observatory: str, path: str = "") -> Path:
    p = Path(path) if path else Path(__file__).parent.parent / "tests" / "data"
    for item in p.iterdir():  # Raises FileNotFoundError
        if item.is_file():
            with fits.open(item) as hdul:
                if observatory == hdul[0].header["ANTENNA"]:
                    return item  # absolute path
    raise ValueError(f"No FITS file produced at {observatory}")


@task(description="Location from FITS file {file_name}")
def location_from_fits(file_name: str) -> EarthLocation:
    with fits.open(file_name) as hdul:
        latitude = hdul[0].header["SiteLatitude"]
        longitude = hdul[0].header["SiteLongitude"]
        height = hdul[0].header["SiteHeight"]

    location = EarthLocation(
        lat=Angle(latitude, unit=u.rad),
        lon=Angle(longitude, unit=u.rad),
        height=height * u.m,
    )
    location.info.name = hdul[0].header["ANTENNA"]
    return location


@task(description="Tune observatory location")
def tune_location(a: EarthLocation, b: EarthLocation) -> EarthLocation:
    a_value = math.sqrt(a.lat.value**2 + a.lon.value**2)
    b_value = math.sqrt(b.lat.value**2 + b.lon.value**2)
    if abs(a_value - b_value) > 10**-3:
        raise ValueError("Locations do not refer the same observatory")

    location = EarthLocation(
        lat=mean([a.lat.value, b.lat.value]),
        lon=mean([a.lon.value, b.lon.value]),
        height=mean([a.height.value, b.height.value]),
    )
    location.info.name = a.info.name
    return location


@task(
    description="Geodetic information of {location.info.name}",
    persist_result=True,
    result_serializer="json",
)
def geodetic_info(location: EarthLocation) -> dict[Any, Any]:
    return {
        "observatory": location.info.name,
        "latitude": location.geodetic.lat.value,
        "longitude": location.geodetic.lon.value,
        "height": location.geodetic.height.value,
    }


@flow(description="Tuned geodetic information of {observatory}")
def tuned_geodetic_info(observatory: str) -> dict[str, Any]:
    logger = get_run_logger()
    logger.setLevel(logging.WARNING)
    loc_from_astropy = location_from_astropy.submit(observatory)
    file_name = observatory_file.submit(observatory)
    loc_from_file = location_from_fits.submit(file_name)
    tuned_location = tune_location(
        loc_from_astropy,
        loc_from_file,
    )
    return geodetic_info(tuned_location)


def cli():
    @click.command()
    @click.option("--observatory", prompt="Tuned Geodetic Info of")
    def procedure(observatory):
        result = tuned_geodetic_info(observatory)
        fres = json.dumps(result, indent=2)  # Formatted result
        click.secho(f"Geodetic_info: {fres}", bg="green", fg="white", bold=True)
        return result

    return procedure
