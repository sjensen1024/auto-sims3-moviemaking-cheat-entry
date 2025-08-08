import time
from dataclasses import dataclass, field
from typing import List
from pynput.keyboard import Key, Controller

@dataclass
class CheatEntry:
    cheats_to_enter: List[str] = field(default_factory=list)
    delay_between_cheats_in_seconds: float = 0
    should_echo_cheat_entry_in_prompt: bool = True

    def enter_cheats(self):
        self.keyboard_controller = Controller()
        for cheat in self.cheats_to_enter:
            self.__process_cheat(cheat)

    def __process_cheat(self, cheat):
        self.__open_cheat_prompt()
        self.__engage_cheat_delay()
        self.keyboard_controller.type(cheat)
        self.__engage_cheat_delay()
        self.keyboard_controller.press(Key.enter)
        self.keyboard_controller.release(Key.enter)
        self.__engage_cheat_delay()
        if self.should_echo_cheat_entry_in_prompt:
             print(f"Cheat processed: {cheat}")

    def __open_cheat_prompt(self):
        self.keyboard_controller.press(Key.ctrl)
        self.keyboard_controller.press(Key.shift)
        self.keyboard_controller.press('c')
        self.keyboard_controller.release('c')
        self.keyboard_controller.release(Key.ctrl)
        self.keyboard_controller.release(Key.shift)

    def __engage_cheat_delay(self):
        time.sleep(self.delay_between_cheats_in_seconds)
