# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '1.0.5.dev0'


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='roosite.launchkit',
    version=version,
    description="A tool to quickly kickstart a Plone based development enviroment",
    long_description=long_description,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='web plone zope skeleton project',
    author='Alteroo',
    author_email='david@alteroo.com',
    url='https://github.com/alteroo/roosite.launchkit',
    license='GPL version 2',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'mr.bob',
    ],
    extras_require={
        'test': [
            'nose',
            'nose-selecttests',
            'scripttest',
            'six',
            'unittest2',
        ]
    },
    entry_points={},
)
