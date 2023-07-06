.. _installation:

How to install Perform
======================

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
