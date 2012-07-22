import sys

__version__ = '0.1a'

def provide_default_settings(application):
    """Inject an application's default settings into django.conf.settings.
    
    Add provide_default_settings(__name__) to __init__.py in your application directory
    and create settings.py inside that directory.
    """
    settings_module = '{}.settings'.format(application)

    try:
        __import__(settings_module)
    except ImportError:
        raise ImportError('Missing settings.py in you app directory. Either '
                          'provide it or delete \'provide_default_settings line '
                          'from __init__.py.\' (module {})'.format(
                                                                settings_module))
    else:
        _app_settings = sys.modules[settings_module]
        _def_settings = sys.modules['django.conf.global_settings']
        _settings = sys.modules['django.conf'].settings

        # Add the values from the application.settings module.
        for key in dir(_app_settings):
            if key.isupper():
                # Check settings name clash.
                if hasattr(_def_settings, key):
                    raise ValueError('Settings name clash, key "{}" already '
                                     'used.'.format(key))

                # Add the value to the default settings module.
                setattr(_def_settings, key, getattr(_app_settings, key))
                
                # Add the value to the settings, if not already present.
                if not hasattr(_settings, key):
                    setattr(_settings, key, getattr(_app_settings, key))
