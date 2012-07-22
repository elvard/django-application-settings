Default Settings for Django Applications
========================================

This repository [1]_ contains a proof of concept Django application that ships
default values for its own settings. This is good for a number of reasons:

1. The application's settings are included in the output of `manage.py
diffsettings`.

2. Application code can just use `settings.MY_SETTING` instead of
`getattr(settings, 'MY_SETTING', 'The default value')`.

3. Application settings are defined in a single place, with sane default
values and, hopefully, with comments. Don't Repeat Yourself!

The actual code is rather simple: it just uses the opportunity afforded it
when the application module is loaded to inject its own default settings into
both the `django.conf.global_settings` module (Django's built-in default
settings, and the source for things like the `diffsettings` management
command) and the `django.conf.settings` object (being careful to check to see
if it already contains a value).

To see more, take a look at:

* `application_settings/__init__.py`_ - the code to provide these defaults.

This is slightly less than a perfect solution (being able to patch
`django.conf.global_settings` *before* `django.conf.settings` is initialised),
but the hypothetical perfection is simply not possible: the settings must be
loaded before they can be used to import the `INSTALLED_APPS`.

.. [1] See original_ repository.

.. _original: http://github.com/thsutton/
.. _application_settings/__init__.py: http://github.com/elvard/django-application-settings/tree/master/application_settings/__init__.py
