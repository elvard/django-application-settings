Default Settings for Django Applications
========================================

This repository contains a proof of concept Django application that ships
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

* [`foo/settings.py`][1] - the default settings for the app.
* [`foo/__init__.py`][2] - the code to inject these defaults.
* [`foo/context_processors.py`][3] - the code that uses these new settings.

This is slightly less than a perfect solution (being able to patch
`django.conf.global_settings` *before* `django.conf.settings` is initialised),
but the hypothetical perfection is simply not possible: the settings must be
loaded before they can be used to import the `INSTALLED_APPS`.

A more complete solution to this problem might allow applications to modify
various settings instead of adding only new settings: things like enabling its
middleware or request context processors by default, for example. Alas, it's
late and I'm tired, so I'll leave that to someone else; this trick is good
enough for my purposes as it stands.

If you have a better solution or know why this is a bad one, please let me
know. [Send me a message on GitHub][msg-gh], [on Twitter][twt], or [by
email][msg-em].

[1]: http://github.com/thsutton/django-application-settings/tree/master/foo/settings.py
[2]: http://github.com/thsutton/django-application-settings/tree/master/foo/__init__.py
[3]: http://github.com/thsutton/django-application-settings/tree/master/foo/context_processors.py

[msg-gh]: http://github.com/inbox/new/thsutton
[twt]: http://www.twitter.com/thsutton
[msg-em]: mailto:me@thomas-sutton.id.au