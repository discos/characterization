.. _dev:

Development Guide
=================

.. topic:: Abstract

   This chapter explains how to contribute to the project.  We welcome
   people eager to write documentation, to define how a particular
   procedure should be performed, and of course to write software.
   The first section of this chapter, :ref:`workflow`, lists the rules
   of thumbs required to implement a procedure.  The chapter terminates
   with the section :ref:`example` that describes a procedure definition
   and implementation.


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
in the :ref:`user` of this manual (file :download:`user.rst`), as you will
see later.

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
Finally, select *Checkout locally* and create the branch.  A pop-up windows
appears showing you the commands to execute in order to ``fetch`` and ``checkout``
the branch locally.

Implementation
~~~~~~~~~~~~~~
The contributor in charge of one task writes the implementation and the tests
related to that task.  You will see later, in section :ref:`example`, how to
properly implement a procedure.

Run ``tox``
~~~~~~~~~~~
Before pushing the code to the procedure's branch, check your code
with ``tox``.  Details are explained in section :ref:`example-tox`.

Push the code and open a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Push the code to the procedure's branch and open a pull request asking for
the code to be merged to the ``main`` branch.

Fix a bug
~~~~~~~~~
If you find a bug in the ``main`` branch, open a GitHub issue that describes
the problem.  To fix the issue, write an automatic test that spots the bug,
then fix the code.


.. _example:

Practical example
-----------------
Let's suppose we want to implement a new procedure called *Tuned Geodetic Information*,
identified by the short name ``example``.

.. _example-share-idea:

Share the idea
~~~~~~~~~~~~~~
We open a GitHub issue where we describe the proposal. `Please have a look
<https://github.com/discos/perform/issues/3>`__.

Write the user documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We open a GitHub issue related to the documentation.  We write the user documentation
in the :download:`user.rst` text file, that you find on the *docs* directory. The
markup language used to format the text file is `reStructuredText
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`__.

After writing the documentation in the *user.rst* file, you should generate
the HTML and check if there are any errors.  To generate the HTML move to the
*docs* directory and run ``make html`` (as usual, the virtual environment has
to be previously activated):

.. code-block:: console

   $ poetry shell  # The venv should be active
   $ cd docs
   $ make html
   Running Sphinx v6.2.1
       ...
   The HTML pages are in _build/html.

The last line of the output refers the location of the generated documentation.
To see the result, open the *index.html* file with your browser.  For instance:

.. code-block:: console

   $ firefox _build/html/index.html

Once the user documentation is completed, close the related GitHub issue.

.. note:: To have a look at the user documentation of this example,
   `look at here <https://discos-perform.readthedocs.io/en/latest/user.html#tuned-geodetic-information-example>`__.  As you can see, before implementing the procedure
   we should already have a clear idea of the user interface.

.. _example-design:

Design
~~~~~~
As described in the `GitHub issue <https://github.com/discos/perform/issues/3>`__,
the procedure takes the name of an observatory (for instance ``SRT``), and returns
the average geodetic information (observatory name, latitude, longitude, height)
of that observatory.  That average information is computed taking in account the
values from Astropy and from a FITS file produced at that observatory.

The procedure can be splitted in 5 independent tasks:

#. ``location_from_astropy(observatory) -> EarthLocation``: this task takes one
   parameter, the name of the observatory, and returns an Astropy class called
   ``EarthLocation``.  That class contains the information of the observatory
   -- such as longitude, latitude, height -- retrieved from the Astropy database.

#. ``observatory_file(observatory) -> file_name``: takes the name of the observatory,
   looks for a FITS file produced at that observatory, and eventually returns the
   name of the first file that has been found.

#. ``location_from_fits(file_name) -> EarthLocation``: takes the file name returned
   by ``observatory_file()``, opens the file and returns an Astropy ``EarthLocation``
   class containing the information of the observatory retrieved from the FITS file.

#. ``tune_location(a, b) -> EarthLocation``: takes two ``EarthLocation`` objects ``a``
   and ``b`` and checks if they refer to the same location.  If they do, it computes
   the average values of longitude, latitude, and height, and returns an
   ``EarthLocation`` containing these average values.

#. ``geodetic_info(EarthLocation) -> dict``: takes an ``EarthLocation`` and reads
   from it the observatory name, latitude, longitude, and height.  It returns a
   Python dictionary containing this information.

By splitting a procedure in independent tasks we can assign each task to
a different collaborator.  In this way the development of the tasks can
progress in parallel.  In addition, the tasks can be executed concurrently,
speeding up the execution time of the proceedure.

Finally, we open 5 GitHub issues, one for each task.

Create a branch for the procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We go to the GitHub page of the procedure and we choose to open a new branch.
The short name of the procedure is ``example``, so we give the branch the name
``example-procedure``.  We select *Checkout locally* and finally create the
branch.  At this point we get the branch locally by executing the following
commands (from the package directory):

.. code-block:: console

   $ git fetch origin
   $ git checkout example-procedure

Implementation
~~~~~~~~~~~~~~
To implement the procedures we use a workflow manager called `Prefect
<https://www.prefect.io/>`__.  Basically, Prefect makes easy splitting the
procedure in smaller tasks.  It has several features, like concurrency,
waiting for task *X* to terminate before executing task *Y*, scheduling,
and so on.

The name given by Prefect to what we have been called procedure is *flow*.
If you have a look at the file :download:`perform/example.py <../perform/example.py>`
you see how the ``example`` procedure has been implemented.

Every task is decorated with the ``task`` decorator, the procedure is decorated
with the ``flow`` decorator.  Here is the procedure:

.. literalinclude:: ../perform/example.py
   :language: python
   :linenos:
   :lines: 89-100

As you can see the procedure is not defined by the name ``example``.  Nevertheless,
the user runs the procedure by giving the name ``example``, as indicated in the
`user documentation
<https://discos-perform.readthedocs.io/en/latest/user.html#tuned-geodetic-information-example>`__.  That's because ``example`` is the name of the module.  So, the name of the
module gives the name to the procedure to be executed by command line.

The five tasks are called sequentially but Perfect, under the hood, executes
them concurrently.  Actually, concurrency happens only when we *submit* the
tasks to the task runner, as in the following case:

.. literalinclude:: ../perform/example.py
   :language: python
   :linenos:
   :lines: 93-94

In fact, when we use ``submit()`` the task runner creates a `future
<https://docs.prefect.io/api-ref/prefect/futures/>`__ and executes
the tasks concurrently.

To understand what happens, we ``import time`` and add a ``time.sleep(5)``
both inside the task ``location_from_astropy()`` and ``observatory_file()``.
We also add the following two lines at the end of the file:

.. code-block:: python

   if __name__ == "__main__":
       tuned_geodetic_info("SRT")

Now we run *example.py* throught the Unix ``time`` command:

.. code-block:: console

   $ time python perform/example.py
       ...
   real	0m7,615s
   user	0m2,979s
   sys	0m1,540s

The real execution time is less than ten seconds because the two tasks with
``time.sleep(5)`` have been executed concurrently.  Now we remove the
``.submit()``:

.. code-block:: python

    loc_from_astropy = location_from_astropy(observatory)
    file_name = observatory_file(observatory)

As you will see, the tasks are going to be executed sequentially:

.. code-block:: console

   $ time python perform/example.py
       ...
   real	0m12,629s
   user	0m2,980s
   sys	0m1,494s

Finally, there is a ``cli()`` function defined at the end of the module.  That
function wraps the procedure in order for it to be called by command line.

.. note:: To see the tests of the ``example`` procedure, have a look at
   :download:`tests/test_example.py <../tests/test_example.py>`.  You can
   use these tests as a template for testing your procedure.

.. _example-tox:

Run ``tox`` to check the ``example`` procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Before pushing the code to the procedure's branch, run ``tox``:

.. code-block:: console

   $ tox
       ...
   py310: OK
   py311: OK
   tests: OK
   docs: OK
   congratulations :)

Tox is configured in order to run the tests with Python 3.10 and 3.11, and of
course it expects that they all pass.  It also checks the coverage, expecting 100%.
It eventually builds the documentation, and verifies that all files -- code,
configuration files and documentation -- are properly formatted.

Push the code and open a pull request
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If ``tox`` is happy, you can commit your code and push it to the repository.
Insert in the commit message the issue ID of your task.  For instance,
if the issue ID of your task is 77, write:

   .. code-block:: console

      $ git commit -m "fix issue 77"

Now push the code to the repository:

   .. code-block:: console

      $ git push origin example-procedure

We pushed to the ``example-procedure`` branch because *example* is the
name of that procedure.  If your procedure is called *foo*, push to the
branch ``foo-procedure``.  Finally, open a pull request asking for the
code to be merged to the ``main`` branch.
