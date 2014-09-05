#!/bin/env python
# -*- coding: utf-8 -*-

'''Django package for jquery:
a fast, small, and feature-rich JavaScript library for HTML
traversal and manipulation, event handling, animation, and Ajax.'''

from setuptools import setup

setup(
    name='django-jquery',
    version='1.11.1',
    url='https://jquery.com',
    description=globals()['__doc__'],
    author='see in AUTHORS.txt',
    maintainer='Renat Galimov',
    maintainer_email='renat2017@gmail.com',
    license='MIT License',
    keywords=['django', 'jquery'],
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_jquery'],
    package_data={
        'django_jquery':
        ['static/django_jquery/js/*',]
    }
)
