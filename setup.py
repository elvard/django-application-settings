#!/usr/bin/env python
# -*- encoding: utf8 -*-

from distutils.core import setup

from application_settings import __version__

setup(
    name='django-application-settings',
    version=__version__,
    description=
        'Providing settings with default values in Django applications',
    author='Tomáš Ehrlich',
    author_email='tomas.ehrlich@gmail.com',
    url='https://github.com/elvard/django-application-settings',
    download_url='https://github.com/elvard/django-application-settings/tarball/0.1a',
    packages=['application_settings'],
    licence='GPL v3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python']
)
