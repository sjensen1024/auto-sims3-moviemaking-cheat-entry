import unittest
from unittest.mock import MagicMock
from src.cheat_entry import CheatEntry
from pynput.keyboard import Key, Controller
import time

class TestCheatEntry(unittest.TestCase):

    def setUp(self):
        self.default_cheats_to_enter = ["hello", "world"]
        self.default_delay_between_cheats_in_seconds = 0.25
        self.original_keyboard_press = Controller.press
        self.original_keyboard_release = Controller.release
        self.original_keyboard_type = Controller.type
        self.original_sleep = time.sleep
        Controller.press = MagicMock(name="keyboard_press")
        Controller.release = MagicMock(name="keyboard_save")
        Controller.type = MagicMock(name="keyboard_type")
        time.sleep = MagicMock(name="sleep")

    def tearDown(self):
        Controller.press = self.original_keyboard_press
        Controller.release = self.original_keyboard_release
        Controller.type = self.original_keyboard_type
        time.sleep = self.original_sleep

    # TODO: Consider if it's worth making it configurable as to whether or not we output that a cheat was processed.
    def test_when_enter_cheats_given_two_cheats_with_quarter_second_delay_and_printing_enabled_then_processes_cheats_and_prints(self):
        cheat_entry = CheatEntry(
            cheats_to_enter = self.default_cheats_to_enter,
            delay_between_cheats_in_seconds = self.default_delay_between_cheats_in_seconds,
            should_echo_cheat_entry_in_prompt = True
        )
        cheat_entry.enter_cheats()
        Controller.press.assert_called()
        Controller.release.assert_called()
        Controller.type.assert_called()
        time.sleep.assert_called()
