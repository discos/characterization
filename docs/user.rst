.. _user:

User Guide
==========

.. topic:: Abstract

   Each section of this chapter explains how to run a particular procedure.
   When you follow the examples, we assume that you are at the root directory
   of the project, and that you have already activated the Pyhon virtual
   environment, as illustrated below:

   .. code-block:: console

      $ cd perform  # Go to the root of the project
      $ poetry shell  # Activate the virtual environment

   Now you run the procedure by executing the command ``perform``
   and giving the name of the procedure, as explained below.


Tuned Geodetic Information - ``example``
-------------------------------------------
This procedure computes and returns the **average** geodetic information of a
given observatory.  That information is computed taking in account the data from
the Astropy library and from a FITS file produced at the observatory.
To see how it works, execute the command ``perform``:

.. code-block:: console

   $ perform
   Procedure name:

The prompt is asking you to enter the name of the procedure.  Type ``example``:

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
