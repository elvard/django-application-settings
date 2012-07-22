DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}
SECRET_KEY = '42'
INSTALLED_APPS = ('testapp',)

TEST_KEY_OVERRIDE = 'Better one!'
