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

First af all, install `Poetry <https://python-poetry.org/>`, a Python package and
dependency manager.  The installation procedure is explained on the `Poetry website
<https://python-poetry.org/docs/#installation>`.

You also need `Git <https://git-scm.com/>` or alternatively the GitHub client.
To install the latter one, follow the instruction that you find `here
https://cli.github.com/manual/installation>`.

Now that Poetry and the GitHub client are installed, clone the `Performance repository
<https://github.com/discos/performance>`::

   $ gh repo clone discos/performance

Install all requirements::

   $ cd performance/
   $ poetry shell
   $ poetry install

Run `tox` to see if everything is properly installed::

   $ tox run

Adding a dependency to a group::



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
