import unittest
from conf_utils.conf import Conf
from conf_utils.env import DJANGO_INSTALLED, DJANGO_CONFIGURED, DJANGO_SETTINGS


class TestConfUtils(unittest.TestCase):
    def test_basic_conf_instance(self):
        test_conf = Conf('test_conf', {
            'TEST_SETTING_1': 1,
            'TEST_SETTING_2': {
                'FOO': 'BAR'
            }
        })
        self.assertEqual(test_conf.TEST_SETTING_1, 1)
        self.assertEqual(test_conf.TEST_SETTING_2, {'FOO': 'BAR'})

    def test_conf_instance_can_be_configured_at_runtime(self):
        test_conf = Conf('test_conf', {})
        self.assertEqual(test_conf.get('TEST_SETTING_1', None), None)
        self.assertEqual(test_conf.get('TEST_SETTING_2', None), None)
        test_conf.configure({
            'TEST_SETTING_1': 1,
            'TEST_SETTING_2': {
                'FOO': 'BAR'
            }
        })
        self.assertEqual(test_conf.get('TEST_SETTING_1', None), 1)
        self.assertEqual(test_conf.get('TEST_SETTING_2', None), {'FOO': 'BAR'})

    def test_django_is_detected_but_is_not_configured_by_default(self):
        self.assertTrue(DJANGO_INSTALLED)
        self.assertFalse(DJANGO_CONFIGURED)
        self.assertEqual(DJANGO_SETTINGS, None)