import time
from dataclasses import dataclass
from pynput.keyboard import Key, Controller

@dataclass
class CheatEntryManager:
    delay_between_cheats_in_seconds: float = 0

    def __post_init__(self):
        self.keyboard_controller = Controller()
        self.is_cheat_prompt_open = False

    def open_cheat_prompt(self):
        self.keyboard_controller.press(Key.ctrl)
        self.keyboard_controller.press(Key.shift)
        self.keyboard_controller.press('c')
        self.keyboard_controller.release('c')
        self.keyboard_controller.release(Key.ctrl)
        self.keyboard_controller.release(Key.shift)
        self.is_cheat_prompt_open = True

    def enter_cheat(self, cheat):
        if not self.is_cheat_prompt_open:
            self.open_cheat_prompt()
        self.__delay_keyboard_presses()
        self.keyboard_controller.type(cheat)
        self.__delay_keyboard_presses()
        self.keyboard_controller.press(Key.enter)
        self.keyboard_controller.release(Key.enter)
        self.is_cheat_prompt_open = False
        self.__delay_keyboard_presses()
        print(f"Cheat processed: {cheat}")

    def __delay_keyboard_presses(self):
        time.sleep(self.delay_between_cheats_in_seconds)
