# -*- encoding: utf-8 -*-
# django-application-settings -- Snippet to provide app's default settings
# Copyright (C) 2012 Tomáš Ehrlich <tomas.ehrlich@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import sys

__version__ = '0.1b'

def provide_default_settings(application):
    """Inject an application's default settings into django.conf.settings.
    
    Add provide_default_settings(__name__) to __init__.py in your application directory
    and create settings.py inside that directory.
    """
    try:
        # Try to import and evaluate settings module.
        from django.conf import settings
        settings.INSTALLED_APPS
    except ImportError:
        # Don't complain about missing settings, as other mechanisms can
        # catch this error. There are cases when no settings are needed,
        # e.g.: during building distributio (python setup.py sdist)
        return

    settings_module = '%s.settings' % application
    try:
        __import__(settings_module)
    except ImportError:
        raise ImportError('Missing settings.py in you app directory. Either '
                          'provide it or delete \'provide_default_settings line\' '
                          'from __init__.py. (module %s)' % settings_module)

    _app_settings = sys.modules[settings_module]
    _def_settings = sys.modules['django.conf.global_settings']
    _settings = sys.modules['django.conf'].settings

    # Add the values from the application.settings module.
    for key in dir(_app_settings):
        if key.isupper():
            # Check settings name clash.
            if hasattr(_def_settings, key):
                raise ValueError('Settings name clash, key %s already '
                                 'used.' % key)

            # Add the value to the default settings module.
            setattr(_def_settings, key, getattr(_app_settings, key))
            
            # Add the value to the settings, if not already present.
            if not hasattr(_settings, key):
                setattr(_settings, key, getattr(_app_settings, key))
