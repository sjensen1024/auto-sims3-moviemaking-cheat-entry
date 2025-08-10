import unittest
from src.configuration import Configuration

class TestConfigManager(unittest.TestCase):
    def test_when_init_given_no_args_then_expect_successful_init_with_default_values(self):
        configuration = Configuration()
        self.assertEqual(len(configuration.cheats_to_enter), 0)
        self.assertEqual(configuration.countdown_in_seconds, 0)
        self.assertEqual(configuration.delay_between_cheats_in_seconds, 0)
        self.assertTrue(configuration.should_auto_open_window)
        self.assertEqual(configuration.window_name, "")

    def test_when_init_given_args_with_allowed_values_then_expect_successful_init_with_given_values(self):
        configuration = Configuration(
            cheats_to_enter = ["hello", "world"],
            countdown_in_seconds = 5,
            delay_between_cheats_in_seconds = 0.25,
            should_auto_open_window = False,
            window_name = "some window"
        )
        self.assertEqual(configuration.cheats_to_enter, ["hello", "world"])
        self.assertEqual(configuration.countdown_in_seconds, 5)
        self.assertEqual(configuration.delay_between_cheats_in_seconds, 0.25)
        self.assertFalse(configuration.should_auto_open_window)
        self.assertEqual(configuration.window_name, "some window")

    def test_when_init_given_negative_countdown_in_seconds_arg_then_expect_raise_value_error(self):
        with self.assertRaises(ValueError):
            Configuration(countdown_in_seconds=-1)

    def test_when_init_given_negative_delay_between_cheats_in_seconds_arg_then_expect_raise_value_error(self):
        with self.assertRaises(ValueError):
            Configuration(delay_between_cheats_in_seconds=-1)
