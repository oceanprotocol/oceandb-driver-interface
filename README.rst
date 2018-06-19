=====================
oceandb-driver-interface
=====================


.. image:: https://img.shields.io/pypi/v/oceandb-driver-interface.svg
        :target: https://pypi.python.org/pypi/oceandb-driver-interface

.. image:: https://img.shields.io/travis/oceanprotocol/oceandb-driver-interface.svg
        :target: https://travis-ci.org/oceanprotocol/oceandb-driver-interface

.. image:: https://readthedocs.org/projects/oceandb-driver-interface/badge/?version=latest
        :target: https://oceandb-driver-interface.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/oceanprotocol/oceandb-driver-interface/shield.svg
     :target: https://pyup.io/repos/github/oceanprotocol/oceandb-driver-interface/
     :alt: Updates



High-level, plugin-bound Ocean DB functions. You should implement a plugin class extending this module to connect with Ocean DB.

* Free software: Apache Software License 2.0
* Documentation: https://oceandb-plugin-system.readthedocs.io.


How to use it
-------------

Abstract interface for all persistence layer plugins.
Expects the following to be defined by the subclass:
        - :attr: type (as a read-only property)
        - :func: write
        - :func: read
        - :func: update
        - :func: delete
        - :func: list

How to develop a plugin
-----------------------

To create a plugin you have to create a class called Plugin extending AbstractPlugin.

You could find an example in plugins/mongo


