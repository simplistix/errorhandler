============
ErrorHandler
============

This is a handler for the python standard logging framework that can
be used to tell whether messages have been logged at or above a
certain level.

This can be useful when wanting to ensure that no errors have been
logged before committing data back to a database.

Here's an example:

First, you set up the error handler:

>>> from logging import getLogger
>>> from errorhandler import ErrorHandler
>>> logger = getLogger()
>>> e = ErrorHandler()

The handler started off being un-fired:

>>> e.fired
False

Then you do whatever else you need to do, which may involve logging:

>>> logger.info('some information')
>>> e.fired
False

However, if any logging occurs at an error level or above:

>>> logger.error('an error')

Then the error handler becomes fired:

>>> e.fired
True

You use this as a condition to only do certain actions when no errors
have been logged:

>>> if e.fired:
...   print "Not updating files as errors have occurred"
Not updating files as errors have occurred

If your code does work in batches, you may wish to reset the error
handler at the start of each batch:

>>> e.reset()
>>> e.fired
False

Finally, it's good practice to remove the handler when you're done,
although this doesn't matter too much:

>>> e.remove()

Once removed, the error handler will not become fired, even 
>>> logger.error('an error')
>>> e.fired
False

The full set of options available when constructing an error handler
is as follows:

``ErrorHandler(level=logging.ERROR,logger='',install=True)``

``level``
  This specifies the logging level at which the error handler will
  fire. Any message logged at or above this level will trigger the
  error handler.

``logger``
  This specifies the logger on which the error handler will be
  installed. The default is the root logger.

``install``
  If True, the handler is automatically installed. If False, the
  handler has to be manually installed by calling its ``install``
  method: 

  >>> e=ErrorHandler(install=False)
  >>> logger.error('an error')
  >>> e.fired
  False
  >>> e.install()
  >>> logger.error('an error')
  >>> e.fired
  True
  >>> e.remove()  
  

Licensing
=========

Copyright (c) 2008 Simplistix Ltd
See license.txt for details.

Changes
=======

1.0.0 (3 Dec 2008)
------------------

- Initial Release
