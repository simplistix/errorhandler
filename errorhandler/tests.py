# Copyright (c) 2008 Simplistix Ltd
#
# This Software is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.html
# See license.txt for more details.

import logging
import unittest
from doctest import DocFileSuite,DocTestSuite,REPORT_NDIFF,ELLIPSIS
from errorhandler import ErrorHandler

class TestErrorHandler:

    def test_level(self):
        """
        The logging level at which the ErrorHandler is fired can also
        be configured: 

        >>> from logging import INFO
        >>> e = ErrorHandler(INFO)

        Debugging messages still don't trigger:
        
        >>> logger.debug('debugging')
        >>> e.fired
        False

        But now informational messages do:

        >>> logger.info('some information')
        >>> e.fired
        True

        >>> e.remove()
        """

    def test_level_greater_than_configured(self):
        """
        Messages logged at levels higher than that configured still
        trigger the handler: 

        >>> from logging import INFO
        >>> e = ErrorHandler(INFO)

        In this case, an ERROR will make a good example:
        
        >>> logger.error('an error')
        >>> e.fired
        True

        >>> e.remove()
        """

    def test_logger_name(self):
        """
        The error handler can be set to only trigger on a certain
        logger and its children:

        >>> from logging import getLogger
        >>> e = ErrorHandler(logger='b')

        Now lets get three loggers:
        
        >>> a = getLogger()
        >>> b = getLogger('b')
        >>> c = getLogger('b.c')

        Logging to `a` won't trigger the handler:
        
        >>> a.critical('message')
        >>> e.fired
        False

        Logging to `b` will trigger the handler:
        
        >>> b.critical('message')
        >>> e.fired
        True
        >>> e.reset()
        >>> e.fired
        False

        Logging to `c` will also trigger the handler:

        >>> c.critical('message')
        >>> e.fired
        True

        >>> e.remove()
        """

    def test_manual_install(self):
        """
        >>> handlers = logging.getLogger().handlers[:]

        You don't have to install when you create:

        >>> e = ErrorHandler(install=False)

        >>> handlers == logging.getLogger().handlers[:]
        True

        You install later by calling the `install` method:

        >>> e.install()

        >>> len(logging.getLogger().handlers[:])-len(handlers)
        1
        
        >>> e.remove()
        """

    def test_install_twice(self):
        """
        >>> handlers = logging.getLogger().handlers[:]

        Installing twice isn't a problem:
        
        >>> e = ErrorHandler()
        >>> len(logging.getLogger().handlers[:])-len(handlers)
        1

        >>> e.install()
        >>> len(logging.getLogger().handlers[:])-len(handlers)
        1
        
        >>> e.remove()
        """

    def test_uninstall(self):
        """
        >>> handlers = logging.getLogger().handlers[:]

        >>> e = ErrorHandler()
        >>> len(logging.getLogger().handlers[:])-len(handlers)
        1

        Uninstalling removes the handler from the handlers list:
        
        >>> e.remove()
        >>> len(logging.getLogger().handlers[:])-len(handlers)
        0
        >>> logging.getLogger().handlers[:]==handlers
        True

        """

    def test_uninstall_twice(self):
        """
        >>> handlers = logging.getLogger().handlers[:]

        Uninstalling twice isn't a problem either:
        
        >>> e = ErrorHandler()
        >>> len(logging.getLogger().handlers[:])-len(handlers)
        1

        >>> e.remove()
        >>> len(logging.getLogger().handlers[:])-len(handlers)
        0
        >>> logging.getLogger().handlers[:]==handlers
        True
        
        >>> e.remove()
        >>> len(logging.getLogger().handlers[:])-len(handlers)
        0
        >>> logging.getLogger().handlers[:]==handlers
        True
        """

original_log_level = None
logger = logging.getLogger()
def setUp(test):
    global original_log_level
    original_log_level = logger.level
    logger.setLevel(logging.DEBUG)

def tearDown(test):
    logger.setLevel(original_log_level)
    
options = REPORT_NDIFF|ELLIPSIS

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('readme.txt',
                     setUp=setUp,
                     tearDown=tearDown,
                     optionflags=options),
        DocTestSuite(setUp=setUp,
                     tearDown=tearDown,
                     optionflags=options),
        ))
