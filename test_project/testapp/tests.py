import unittest

class AppSettingsUnitTest(unittest.TestCase):
    def test_provide_application_default(self):
        from django.conf import settings
        from testapp import settings as app_settings
        from test_project import settings as project_settings

        for k, v in app_settings.__dict__.items():
            if not k.isupper(): continue

            value = getattr(project_settings, k, v)

            self.assertTrue(hasattr(settings, k))
            self.assertEqual(getattr(settings, k), value)
