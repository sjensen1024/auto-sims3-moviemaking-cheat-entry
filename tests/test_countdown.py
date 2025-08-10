import unittest
from unittest.mock import MagicMock, call
from src.countdown import Countdown
import time

class TestCountdown(unittest.TestCase):
    def setUp(self):
        self.original_sleep = time.sleep
        time.sleep = MagicMock(name="sleep")

    def tearDown(self):
        time.sleep = self.original_sleep

    def test_when_init_given_no_total_seconds_args_then_total_seconds_should_be_set_to_ten(self):
        self.assertEqual(Countdown().total_seconds, 10)

    def test_when_init_given_total_seconds_is_negative_then_total_seconds_should_be_set_to_ten(self):
        self.assertEqual(Countdown(total_seconds=-1).total_seconds, 10)

    def test_when_init_given_total_seconds_is_zero_then_total_seconds_should_be_set_to_ten(self):
        self.assertEqual(Countdown(total_seconds=0).total_seconds, 10)

    def test_when_init_given_total_seconds_is_greater_than_zero_then_total_seconds_should_be_set_to_that_number(self):
        self.assertEqual(Countdown(total_seconds=1).total_seconds, 1)

    def test_when_start_given_seconds_is_five_then_sleep_should_sleep_for_one_second_five_times(self):
        Countdown(total_seconds=5).start()
        self.assertEqual(time.sleep.call_args_list.count(call(1)), 5)
