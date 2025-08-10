import unittest
from unittest.mock import MagicMock, call, patch
from src.countdown import Countdown
from src.game_window import GameWindow
from src.cheat_entry import CheatEntry
from src.process import Process

class TestProcess(unittest.TestCase):
    def setUp(self):
        self.test_config_file_directory = "\\tests\\support\\config\\"
        self.original_enter_cheat = CheatEntry.enter_cheat
        self.original_bring_window_to_front = GameWindow.bring_window_to_front
        self.original_countdown_start = Countdown.start
        CheatEntry.enter_cheat = MagicMock("enter_cheat")
        GameWindow.bring_window_to_front = MagicMock("bring_window_to_front")
        Countdown.start = MagicMock("countdown_start")

    def tearDown(self):
        CheatEntry.enter_cheat = self.original_enter_cheat
        GameWindow.bring_window_to_front = self.original_bring_window_to_front
        Countdown.start = self.original_countdown_start

    def test_when_run_given_configuration_has_should_auto_show_window_true_then_should_run_process_and_auto_show_window(self):
        config_path = self.test_config_file_directory + "cheat_entry_config_with_true_should_auto_show_window.yml"
        process = Process(config_path_relative_to_project_root=config_path)
        process.run()
        self.assert_common_process_attributes_are_set_up_correctly(process)
        self.assertEqual(process.game_window.window_name, "my window")
        GameWindow.bring_window_to_front.assert_called()


    def test_when_run_given_configuration_has_should_auto_show_window_false_then_should_run_process_without_auto_showing_window(self):
        config_path = self.test_config_file_directory + "cheat_entry_config_with_false_should_auto_show_window.yml"
        process = Process(config_path_relative_to_project_root=config_path)
        process.run()
        self.assert_common_process_attributes_are_set_up_correctly(process)
        GameWindow.bring_window_to_front.assert_not_called()

    def assert_common_process_attributes_are_set_up_correctly(self, process):
        self.assertEqual(process.countdown.total_seconds, 5)
        self.assertEqual(process.cheat_entry.delay_between_cheats_in_seconds, 0.5)
        Countdown.start.assert_called()
        self.assertEqual(CheatEntry.enter_cheat.call_args_list.count(call("cheat 1")), 1)
        self.assertEqual(CheatEntry.enter_cheat.call_args_list.count(call("cheat 2")), 1)
        