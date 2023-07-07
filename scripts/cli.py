from __future__ import annotations

import argparse
import importlib
import pathlib
import sys

import click

parser = argparse.ArgumentParser(
    description="Perform antenna characterization",
    usage="just run 'perform', no arguments are required",
)
args = parser.parse_args()


def procedures():
    procedures = []
    p = pathlib.Path(__file__).parent.parent / "perform"
    for item in p.iterdir():  # Raises FileNotFoundError
        if item.is_file():
            name = item.name
            if name.endswith(".py") and not name.startswith("_"):
                procedure = name.rstrip(".py")
                procedures.append(procedure)
    return procedures


@click.command()
@click.option("--name", prompt="Procedure name")
def perform(name):
    try:
        module = importlib.import_module(f"perform.{name}")
    except ModuleNotFoundError:
        click.secho(f"\nERROR: procedure '{name}' does not exist", fg="red", bold=True)
        print("Available procedures:")
        for procedure in procedures():
            click.secho(f" * {procedure}", fg="green")
        sys.exit(1)
    cli = getattr(module, "cli")
    procedure = cli()
    procedure()


if __name__ == "__main__":
    perform()
