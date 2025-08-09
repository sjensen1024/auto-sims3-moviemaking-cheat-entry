import unittest
from unittest.mock import MagicMock, call, patch
from src.game_window_manager import GameWindowManager
import win32gui

class TestGameWindowManager(unittest.TestCase):
    def setUp(self):
        self.original_show_window = win32gui.ShowWindow
        self.original_set_foreground_window = win32gui.SetForegroundWindow
        self.original_get_window_text = win32gui.GetWindowText
        win32gui.ShowWindow = MagicMock("show_window")
        win32gui.SetForegroundWindow = MagicMock("set_foreground_window")
        win32gui.GetWindowText = MagicMock("get_window_text")

    def tearDown(self):
        win32gui.ShowWindow = self.original_show_window
        win32gui.SetForegroundWindow = self.original_set_foreground_window
        win32gui.GetWindowText = self.original_get_window_text

    def test_when_init_given_no_window_name_then_use_default_window_name(self):
        game_window_manager = GameWindowManager()
        self.assertEqual(game_window_manager.window_name, 'the sims 3')

    def test_when_init_given_window_name_of_none_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            GameWindowManager(window_name = None)

    def test_when_init_given_window_name_of_empty_string_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            GameWindowManager(window_name = '')

    def test_when_init_given_window_name_of_only_whitespace_then_raise_value_error(self):
        with self.assertRaises(ValueError):
            GameWindowManager(window_name = "  ")

    def test_when_init_given_window_name_of_some_window_then_returns_some_window(self):
        game_window_manager = GameWindowManager(window_name="some window")
        self.assertEqual(game_window_manager.window_name, "some window")

    def test_when_bring_window_to_front_given_window_not_found_then_does_not_try_to_bring_window_to_front(self):
        game_window_manager = GameWindowManager(window_name="some window")
        with patch('win32gui.EnumWindows') as mock_enumwindows:
            def mock_enum_windows_side_effect(callback, extra):
                callback("other window", extra)
            mock_enumwindows.side_effect = mock_enum_windows_side_effect
            win32gui.GetWindowText.return_value = "other window"
            game_window_manager.bring_window_to_front()
            win32gui.GetWindowText.assert_called()
            win32gui.ShowWindow.assert_not_called()
            win32gui.SetForegroundWindow.assert_not_called()
    
    def test_when_bring_window_to_front_given_window_found_then_brings_window_to_front(self):
        game_window_manager = GameWindowManager(window_name="some window")
        with patch('win32gui.EnumWindows') as mock_enumwindows:
            def mock_enum_windows_side_effect(callback, extra):
                callback("some window", extra)
            mock_enumwindows.side_effect = mock_enum_windows_side_effect
            win32gui.GetWindowText.return_value = "some window"
            game_window_manager.bring_window_to_front()
            win32gui.GetWindowText.assert_called()
            win32gui.ShowWindow.assert_called()
            win32gui.SetForegroundWindow.assert_called()
                        