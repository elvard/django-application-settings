import unittest

from application_settings import autodiscover_settings

class AppSettingsUnitTest(unittest.TestCase):
    def test_autodiscover_settings(self):
        autodiscover_settings()

        from django.conf import settings
        from autodiscoverapp import settings as app_settings
        from test_project import settings as project_settings

        for k, v in app_settings.__dict__.items():
            if not k.isupper(): continue

            value = getattr(project_settings, k, v)

            self.assertTrue(hasattr(settings, k))
            self.assertEqual(getattr(settings, k), value)
