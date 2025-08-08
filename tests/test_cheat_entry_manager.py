import unittest
from unittest.mock import MagicMock, call
from src.cheat_entry_manager import CheatEntryManager
from pynput.keyboard import Key, Controller
import time

class TestCheatEntry(unittest.TestCase):
    def setUp(self):
        self.cheat_entry_manager = CheatEntryManager(delay_between_cheats_in_seconds=0.25)
        self.original_keyboard_press = Controller.press
        self.original_keyboard_release = Controller.release
        self.original_keyboard_type = Controller.type
        self.original_sleep = time.sleep
        self.original_open_cheat_prompt = CheatEntryManager.open_cheat_prompt
        CheatEntryManager.open_cheat_prompt = MagicMock(name="open_cheat_prompt")
        Controller.press = MagicMock(name="keyboard_press")
        Controller.release = MagicMock(name="keyboard_save")
        Controller.type = MagicMock(name="keyboard_type")
        time.sleep = MagicMock(name="sleep")

    def tearDown(self):
        Controller.press = self.original_keyboard_press
        Controller.release = self.original_keyboard_release
        Controller.type = self.original_keyboard_type
        time.sleep = self.original_sleep
        CheatEntryManager.open_cheat_prompt = self.original_open_cheat_prompt

    def test_when_open_cheat_prompt_then_should_open_cheat_prompt(self):
        CheatEntryManager.open_cheat_prompt = self.original_open_cheat_prompt
        self.cheat_entry_manager.open_cheat_prompt()
        self.__assert_key_is_pressed_and_released_a_certain_number_of_times(Key.ctrl, 1)
        self.__assert_key_is_pressed_and_released_a_certain_number_of_times(Key.shift, 1)
        self.__assert_key_is_pressed_and_released_a_certain_number_of_times('c', 1)
        self.assertTrue(self.cheat_entry_manager.is_cheat_prompt_open)

    def test_when_enter_cheat_given_cheat_prompt_is_open_then_should_enter_cheat_without_opening_cheat_prompt_and_close_cheat_prompt(self):
        self.cheat_entry_manager.is_cheat_prompt_open = True
        self.cheat_entry_manager.enter_cheat("Hello")
        CheatEntryManager.open_cheat_prompt.assert_not_called()
        self.__assert_sleep_and_keyboard_methods_are_called_and_cheat_entry_prompt_is_closed("Hello")
        
    def test_when_enter_cheat_given_cheat_prompt_is_not_open_then_should_open_cheat_prompt_and_enter_cheat_and_close_cheat_prompt(self):
        self.cheat_entry_manager.enter_cheat("Hello")
        CheatEntryManager.open_cheat_prompt.assert_called()
        self.__assert_sleep_and_keyboard_methods_are_called_and_cheat_entry_prompt_is_closed("Hello")

    def __assert_sleep_and_keyboard_methods_are_called_and_cheat_entry_prompt_is_closed(self, expected_cheat):
        self.assertEqual(time.sleep.call_args_list.count(call(0.25)), 3)
        self.__assert_key_is_pressed_and_released_a_certain_number_of_times(Key.enter, 1)
        self.assertEqual(Controller.type.call_args_list.count(call(expected_cheat)), 1)
        self.assertFalse(self.cheat_entry_manager.is_cheat_prompt_open)

    def __assert_key_is_pressed_and_released_a_certain_number_of_times(self, expected_key, expected_number_of_times):
        self.assertEqual(Controller.press.call_args_list.count(call(expected_key)), expected_number_of_times)
        self.assertEqual(Controller.release.call_args_list.count(call(expected_key)), expected_number_of_times)
