|banner|

.. raw:: html

   <h1 align="center">

oceandb-driver-interface

.. raw:: html

   </h1>

..

    🐳 Ocean DB driver interface(Python).

.. |banner| image:: docs/imgs/repo-banner@2x.png
   :target: https://oceanprotocol.com

.. image:: https://img.shields.io/pypi/v/oceandb-driver-interface.svg
        :target: https://pypi.python.org/pypi/oceandb-driver-interface

.. image:: https://img.shields.io/travis/oceanprotocol/oceandb-driver-interface.svg
        :target: https://travis-ci.com/oceanprotocol/oceandb-driver-interface

.. image:: https://readthedocs.org/projects/oceandb-driver-interface/badge/?version=latest
        :target: https://oceandb-driver-interface.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status





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

You could find an example in https://github.com/oceanprotocol/oceandb-bigchaindb-driver


