# Copyright (c) 2008-2009 Simplistix Ltd, 2016 Chris Withers
# See license.txt for license details.

import os
from setuptools import setup

package_name = 'errorhandler'
base_dir = os.path.dirname(__file__)

setup(
    name=package_name,
    version=open(os.path.join(base_dir,package_name,'version.txt')).read().strip(),
    author='Chris Withers',
    author_email='chris@simplistix.co.uk',
    license='MIT',
    description="A logging framework handler that tracks when messages above a certain level have been logged.",
    long_description=open(os.path.join(base_dir,'docs','description.txt')).read(),
    url='https://github.com/Simplistix/errorhandler',
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    ],    
    packages=[package_name],
    zip_safe=False,
    include_package_data=True,
    extras_require=dict(
        test=['nose', 'nose-fixes', 'nose-cov', 'coveralls'],
        build=['sphinx', 'pkginfo', 'setuptools-git', 'wheel', 'twine']
    )
)
