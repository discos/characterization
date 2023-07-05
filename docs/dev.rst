.. _dev:

Development Guide
=================

.. topic:: Abstract

   This chapter explains how to contribute to the project.  We welcome
   people eager to write documentation, to define how a particular
   procedure should be performed, and of course to write software.
   The first section of this chapter concerns the installation of the
   `Perform <https://github.com/discos/perform>`_ package and
   later on, in the section :ref:`workflow`, there is a listing of rules
   of thumbs required to implement a procedure.  The chapter terminates
   with the section :ref:`example` that describes a procedure definition
   and implementation.  That example shows how to put in practice the steps
   you have learned in theory.


Installation
------------

First af all, install `Poetry <https://python-poetry.org/>`_, a Python package and
dependency manager.  The installation procedure is explained on the `Poetry website
<https://python-poetry.org/docs/#installation>`_.
You also need the `GitHub client <https://cli.github.com/>`_ (or alternatively
`Git <https://git-scm.com/>`_).  To install the latter one, follow the instruction
available `here <https://cli.github.com/manual/installation>`_.

Now that Poetry and the GitHub client are installed, clone the `Perform repository
<https://github.com/discos/perform>`_:

.. code-block:: console

   $ gh repo clone discos/perform

Install all requirements:

.. code-block:: console

   $ cd perform/
   $ poetry shell
   $ poetry install

The command ``poetry shell`` creates a ``.venv`` virtual environment directory
inside the current directory.  The command ``poetry install`` installs all
dependencies into the virtual environment.

Finally, run ``tox`` to see if everything is working properly:

.. code-block:: console

   $ tox run

You have green light when no errors are reported at the end of the ``tox`` output.


.. _workflow:

Workflow
--------
By the word *procedure* we mean a software operation that measures an antenna
characteristic, such as *beam shape* or *gain*.  This section explains the
guidelines to be followed in order to write a procedure.

Share the idea
~~~~~~~~~~~~~~
When you want to implement a new procedure, as a first step you share your
idea by writing the proposal as a GitHub issue, `by opening a new issue
<https://github.com/discos/perform/issues/new>`_ on the GitHub repository.
The proposal description should be as clear as possible, all contributors
(astronomers, software developers, people in charge of the documentation)
must be able to understand what the procedure is supposed to do and the
motivation.

Once you wrote the GitHub issue, the contributors evaluate the proposal and
start a discussion by commenting the proposal on the issue's page. The proposal
can be improved and finally approved, or even discarded.  It is adviced to set
a short deadline for the decision to be taken.  Once the proposal is approved,
the procedure has to be properly documented before the implementation starts.

Documentation
~~~~~~~~~~~~~
We open a GitHub issue related to the documentation that we are supposed to
write, then we write the documentation describing the procedure from
the user point of view.  It means that we should indicate how the user runs
the procedure, the meaning of the parameters, the description of the result,
some examples of execution, and so on. This documentation has to be written
in the :ref:`user` of this manual (file :download:`user.rst`).

Design
~~~~~~
Once the user documentation of the procedure is completed, we analize the
procedure in order to split it in small and independend *N* tasks.
We hopefully have *N* contributors working in parallel, one contributor
taking care of one single task.  Each task must have its own GitHub issue
that describes what the task is supposed to do.  Eventually we have *N+1*
open issues, one for the procedure, and one for every task composing the
procedure.  Finally, for every task we decide how to automatically test it.

Create a branch for the procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Go to the GitHub issue page of the procedure and create a new branch for the
issue (right side of the page, under the section *Development*). If the
procedure is called ``foo``, give the branch the name ``foo-procedure``.

Implementation
~~~~~~~~~~~~~~
The contributor in charge of one task writes the implementation and the tests
related to that task.  You will see later, in section :ref:`example`, how to
write the tests.

Run ``tox``
~~~~~~~~~~~
Before pushing the code to the procedure's branch, check your code
with ``tox``.  See the section :ref:`example-tox`.

Push the code and open a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Push the code to the procedure's branch and open a pull request asking for
the code to be merged on the ``main`` branch.

Fix a bug
~~~~~~~~~
If you find a bug in the ``main`` branch, open a GitHub issue that describes
the problem.  To fix the issue, write an automatic test that spots the bug,
then fix the code.


.. _example:

Practical example
-----------------
Let's suppose we want to implement a new procedure called *Tuned Geodetic Information*.

.. _example-share-idea:

Share the idea
~~~~~~~~~~~~~~
We open a GitHub issue where we describe the proposal. `Please have a look
<https://github.com/discos/perform/issues/3>`__.


.. _example-design:

The design of foo
~~~~~~~~~~~~~~~~~
* extract the user story
* define the tasks
* write the flow
* write the tests
* tox
* write the user documentation


.. _example-tox:

Run ``tox`` to check the ``example`` procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
foo...

User Story
~~~~~~~~~~
We want a command ``tuned_location_info LOCATION``.
This command returns the tuned information of a given location.
