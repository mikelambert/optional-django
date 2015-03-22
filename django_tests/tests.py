import unittest
from conf_utils.conf import Conf
from conf_utils.env import DJANGO_INSTALLED, DJANGO_CONFIGURED, DJANGO_SETTINGS


class TestConfUtilsDjangoIntegration(unittest.TestCase):
    def test_django_is_detected_and_the_env_is_setup(self):
        self.assertTrue(DJANGO_INSTALLED)
        self.assertTrue(DJANGO_CONFIGURED)
        self.assertNotEqual(DJANGO_SETTINGS, None)

    def test_namespaces_can_have_default_values_overridden(self):
        test_overrides = Conf('TEST_OVERRIDES', {
            'FOO': 'NOT-BAR',
            'BAR': 1,
        })
        self.assertEqual(test_overrides.FOO, 'BAR')
        self.assertEqual(test_overrides.BAR, 1)