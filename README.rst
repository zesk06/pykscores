========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/pykscores/badge/?style=flat
    :target: https://readthedocs.org/projects/pykscores
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/zesk06/pykscores.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/zesk06/pykscores

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/zesk06/pykscores?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/zesk06/pykscores

.. |codecov| image:: https://codecov.io/github/zesk06/pykscores/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/zesk06/pykscores

.. |version| image:: https://img.shields.io/pypi/v/pykscores.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pykscores

.. |commits-since| image:: https://img.shields.io/github/commits-since/zesk06/pykscores/vv0.2.0..svg
    :alt: Commits since latest release
    :target: https://github.com/zesk06/pykscores/compare/vv0.2.0....master

.. |wheel| image:: https://img.shields.io/pypi/wheel/pykscores.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pykscores

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pykscores.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pykscores

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pykscores.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pykscores


.. end-badges

A python3 app to keep game scores

* Free software: Apache Software License 2.0

Installation
============

::

    pip install pykscores

Documentation
=============

https://pykscores.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
