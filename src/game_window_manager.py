import win32gui
import win32con
from dataclasses import dataclass

@dataclass
class GameWindowManager:
    window_name: str = "the sims 3"

    def __post_init__(self):
        if self.window_name is None:
            raise ValueError("window_name cannot be None")
        if not self.window_name.strip():
            raise ValueError("window_name cannot be an empty string")
        self.not_found_value = "The window could not be found"

    def get_window(self):
        top_windows = []
        win32gui.EnumWindows(self.__window_enum_handler, top_windows)
        for i in top_windows:
            if self.window_name.lower() in i[1].lower():
                return i[0]
        
        return self.not_found_value

    def bring_window_to_front(self):
        found_window = self.get_window()
        if found_window == self.not_found_value:
            print(
                "We could not find a window with a name including '" + 
                self.window_name + 
                "' . Ensure there is a window running and open it.")
            return
    
        win32gui.ShowWindow(found_window, win32con.SW_SHOWNORMAL)
        win32gui.SetForegroundWindow(found_window)

    def __window_enum_handler(self, hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
