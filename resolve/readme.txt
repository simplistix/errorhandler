=======
Resolve
=======

This small package seeks to encapsulate code that resolves a string
containing a dotted name into the patching python object in one
place. 

Having seen variants of this type of code duplicated in so many
places, the author decided to make one package with this as its sole
purpose. 

If your use case isn't met by `resolve`, please let the author no and
a new version that caters for your requirement will be released as
soon as possible!

To install resolve, do one of:

- `easy_install resolve`

- add `resolve` as a required egg in your buildout config.

- download the appropriate resolve.tar.gz from 

  http://pypi.python.org/pypi/resolve

  You'll then need to unpack it and do the usual 
  `python setup.py install`

Examples
========

>>> from resolve import resolve

>>> resolve('unittest')
<module 'unittest' from '...'>

>>> resolve('datetime.datetime')
<type 'datetime.datetime'>

>>> resolve('datetime.datetime.now')
<built-in method now of type object at 0x1E1C9D88>

>>> resolve('non existent module')
Traceback (most recent call last):
...
ImportError: No module named non existent module

>>> resolve('__doc__')
Traceback (most recent call last):
...
ImportError: No module named __doc__

>>> resolve('datetime.foo')
Traceback (most recent call last):
...
AttributeError: 'module' object has no attribute 'foo'

Licensing
=========

Copyright (c) 2008 Simplistix Ltd
See license.txt for details.

Changes
=======

1.0.0
-----

- Initial Release
