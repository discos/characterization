.. _user:

User Guide
==========

.. topic:: Abstract

   Each section of this chapter explains how to run a particular procedure.
   You should execute the commands from root directory of the project.
   The Python virtual environment should be active. Summarizing:

   .. code-block:: console

      $ cd perform  # Go to the root of the project
      $ poetry shell  # Activate the virtual environment

   As you will see later on, the procedures are executed by the command ``perform``.


Tuned Geodetic Information - ``example``
----------------------------------------
Before explaining how to use this procedure, we take a few minutes to illustrate
the rationale.  Let's start looking at the ``EarthLocation`` class of the `Astropy
<https://www.astropy.org/>`__ library.  It gives information about an
observatory, as you can see here:

.. code-block:: python

   >>> from astropy.coordinates import EarthLocation
   >>> srt = EarthLocation.of_site("SRT")
   >>> srt.info.name
   'Sardinia Radio Telescope'
   >>> srt.height
   <Quantity 671.6665 m>

The height of SRT, according to Astropy, is ``671.6665`` meters.  That height is
not the same as the one saved on the FITS files generated from DISCOS:

.. code-block:: python

   >>> from astropy.io import fits
   >>> hdul = fits.open('tests/data/xyz.fits')
   >>> hdul[0].header["ANTENNA"]
   'SRT'
   >>> hdul[0].header["SiteHeight"]
   650.0

That is why we implemented the ``example`` procedure.  In fact ``example`` computes
and returns the **average** geodetic information of a given observatory.  That
information is computed taking in account the data from the Astropy library and
from a FITS file produced at the observatory.  To see how it works, execute the
command ``perform``:

.. code-block:: console

   $ perform
   Procedure name:

The prompt is asking us to enter the name of the procedure.  We type ``example``:

.. code-block:: console

   $ perform
   Procedure name: example
   Tuned Geodetic Info of:

The prompt is now asking to enter the observatory name.  We give the name
``SRT`` and finally get the average geodetic information of SRT:

.. code-block:: console

   $ perform
   Procedure name: example
   Tuned Geodetic Info of: SRT
      ...
   Geodetic_info: {
       "observatory": "Sardinia Radio Telescope",
       "latitude": 39.493056194999994,
       "longitude": 9.245155620000004,
       "height": 660.8332500009775
   }

.. note:: The user documentation of this procedure is just an example, use
   it as a reference template.
