.. _dev:

Development Guide
=================

.. topic:: Abstract

   This chapter explains how to develop a procedure.  It is divided
   in several sections, one for each step required for implementing
   the procedure. Let's suppose we really have to implement a procedure,
   that we call *Tune location info*.

Description
-----------
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
