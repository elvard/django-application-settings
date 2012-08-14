DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}
SECRET_KEY = '42'
INSTALLED_APPS = ('testapp', 'autodiscoverapp')

TEST_KEY_OVERRIDE = 'Better one!'
TEST_AUTO_KEY_OVERRIDE = 'So long and thanks for all the fish!'
