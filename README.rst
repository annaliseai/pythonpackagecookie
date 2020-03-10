============================
Python Package Cookiecutter
============================


Harrison.ai Cookiecutter_ template for a Python package.  This cookiecutter
provides a fast, easy way to start a new Python package with all of the build
and development environment settings ready to go out of the box.  

* Github repo:  https://github.com/AnnaliseAI/pythonpackagecookie.git

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* Buildkite build templates: Ready for Buildkite CICD
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Versioneer_ : Pre-configured version bumping with a single command
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Versioneer: https://github.com/warner/python-versioneer
.. _ReadTheDocs: https://readthedocs.org/

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/AnnaliseAI/pythonpackagecookie.git

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
