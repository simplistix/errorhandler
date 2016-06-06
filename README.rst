|Travis|_ |Coveralls|_ |Docs|_ |PyPI|_

.. |Travis| image:: https://api.travis-ci.org/Simplistix/errorhandler.svg?branch=master
.. _Travis: https://travis-ci.org/Simplistix/errorhandler

.. |Coveralls| image:: https://coveralls.io/repos/Simplistix/errorhandler/badge.svg?branch=master
.. _Coveralls: https://coveralls.io/r/Simplistix/errorhandler?branch=master

.. |Docs| image:: https://readthedocs.org/projects/errorhandler/badge/?version=latest
.. _Docs: http://errorhandler.readthedocs.org/en/latest/

.. |PyPI| image:: https://badge.fury.io/py/errorhandler.svg
.. _PyPI: https://badge.fury.io/py/errorhandler
    
ErrorHandler
============

This is a handler for the python standard logging framework that can
be used to tell whether messages have been logged at or above a
certain level.

This can be useful when wanting to ensure that no errors have been
logged before committing data back to a database.

As an example, first, you set up the error handler:

>>> from errorhandler import ErrorHandler
>>> e = ErrorHandler()

Then you can log and check the handler at any point to see if it has
been triggered:

>>> e.fired
False
>>> from logging import getLogger
>>> logger = getLogger()
>>> logger.error('an error')
>>> e.fired
True

You can use the `fired` attribute to only perform actions when no
errors have been logged:

>>> if e.fired:
...   print "Not updating files as errors have occurred"
Not updating files as errors have occurred

Installation
============

Do the following in your virtualenv::

  pip install errorhandler

Documentation
=============

The latest documentation can also be found at:
http://errorhandler.readthedocs.org/en/latest/

Licensing
=========

Copyright (c) 2008-2015 Simplistix Ltd, 2016 Chris Withers.
See docs/license.txt for details.
