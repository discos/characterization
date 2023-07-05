.. _dev:

Development Guide
=================

.. topic:: Abstract

   This chapter explains how to contribute to the project.  We welcome
   people eager to write documentation, to define how a particular
   procedure should be performed, and of course to write software.
   The first section of this chapter concerns the installation of the
   `Performe <https://github.com/discos/performe>`_ package and
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
that you find `here <https://cli.github.com/manual/installation>`_.

Now that Poetry and the GitHub client are installed, clone the `Performe repository
<https://github.com/discos/performe>`_:

.. code-block:: console

   $ gh repo clone discos/performe

Install all requirements:

.. code-block:: console

   $ cd performe/
   $ poetry shell
   $ poetry install

The command ``poetry shell`` created a ``.venv`` virtual environment directory
inside the current directory.  The command ``poetry install`` installed all
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
<https://github.com/discos/performe/issues/new>`_ on the GitHub repository.
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
The documentation starts describing the procedure from the user point of
view.  It means that we should write how the user runs the procedure, what
the meaning of the parameters is, the description of the result, some
examples of execution, and so on. This documentation has to be written in the
:ref:`user` part of this manual.

Design
~~~~~~
Once the procedure interface is clearly documented from the user point of view,
we see how to split the procedure in small and independend *N* tasks.
For every task we decide how to automatically test it.  We hopefully have
*N* contributors working in parallel, one contributor taking care of one
single task. Each task must have its own GitHub issue that describes what
the task is supposed to do. Eventually we have *N+1* open issues, one for
the procedure and one for every task composing the procedure.

Create a branch for the procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementation
~~~~~~~~~~~~~~
The contributor in charge of one task writes the implementation and the tests
related to that task.  The commits have to be pushed on a new branch, giving
to that branch the name ``fix-issue-K``, where *K* is the ID of the issue.
Eventually, the collaborator opens a pull request asking for the code to be
merged on the ``main`` branch. As you will see later, some automatic checks
are performed before the commit terminates, and the commit aborts in case
of no proper code formatting.

Tox
~~~~~~~
Esecuzione dei test etc.
How to write the tests.
Before commit.
How to commit
How to push
How to merge.


.. _example:

Practical example
-----------------
Let's suppose we want to implement a new procedure called *Tuned Geodetic Information*.

.. _example-share-idea:

Share the idea
~~~~~~~~~~~~~~
We open a GitHub issue where we describe the proposal. `Please have a look
<https://github.com/discos/performe/issues/3>`__.



.. _example-design:

The design of foo
~~~~~~~~~~~~~~~~~
* extract the user story
* define the tasks
* write the flow
* write the tests
* tox
* write the user documentation

User Story
~~~~~~~~~~
We want a command ``tuned_location_info LOCATION``.
This command returns the tuned information of a given location.
