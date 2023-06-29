.. _dev:

Development Guide
=================

.. topic:: Abstract

   This chapter explains how to contribute to the project. We welcome
   people eager to write documentation, to define how a particular
   procedure should be performed, to write software, and so on.
   The first section of this chapter concerns the installation of the
   package. Once Performance is properly installed you will be guided
   through an example of procedure definition and implementation.
   That example shows the development workflow, in order for you
   to know the steps required to develop a new procedure from scratch.

Installation
------------

First af all, install `Poetry <https://python-poetry.org/>`_, a Python package and
dependency manager.  The installation procedure is explained on the `Poetry website
<https://python-poetry.org/docs/#installation>`_.

You also need `Git <https://git-scm.com/>`_ or alternatively the GitHub client.
To install the latter one, follow the instruction that you find `here
<https://cli.github.com/manual/installation>`_.

Now that Poetry and the GitHub client are installed, clone the `Performance repository
<https://github.com/discos/performance>`_:

.. code-block:: console

   $ gh repo clone discos/performance

Install all requirements:

.. code-block:: console

   $ cd performance/
   $ poetry shell
   $ poetry install

The command ``poetry shell`` created a ``.venv`` virtual environment directory
inside the current directory.  The command ``poetry install`` installed all
dependencies into the virtual environment.

Finally, run ``tox`` to see if everything is working properly:

.. code-block:: console

   $ tox run

No errors should be reported at the end of the ``tox`` output.


Next section
------------
Let's suppose we want to implement a new procedure.  That procedure
does... define it.
We open an issue on GitHub describing the procedure
we want to implement.

The rest
--------
* extract the user story
* define the tasks
* write the flow
* write the tests
* tox
* write the user documentation

Example of command ``tuned_location_info``
------------------------------------------

User Story
~~~~~~~~~~
We want a command ``tuned_location_info LOCATION``.
This command returns the tuned information of a given location.
