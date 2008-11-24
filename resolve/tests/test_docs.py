# Copyright (c) 2008 Simplistix Ltd
#
# This Software is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.html
# See license.txt for more details.

import unittest
from doctest import DocFileSuite, REPORT_NDIFF,ELLIPSIS

options = REPORT_NDIFF|ELLIPSIS

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('../readme.txt', optionflags=options),
        ))
