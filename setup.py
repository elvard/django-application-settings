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
    download_url='https://github.com/downloads/elvard/django-application-settings/django-application-settings-0.1b.tar.gz',
    packages=['application_settings'],
    license='GPL v3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python']
)
