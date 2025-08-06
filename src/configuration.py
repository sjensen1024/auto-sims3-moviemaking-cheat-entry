from dataclasses import dataclass, field
from typing import List

@dataclass
class Configuration:
    cheats_to_enter: List[str] = field(default_factory=list)
    delay_between_cheats_in_seconds: float = 0
    should_echo_cheat_entry_in_prompt: bool = True
    countdown_in_seconds: float = 0
    should_auto_open_window: bool = True
    window_name: str = ""

    def __post_init__(self):
        self.__raise_error_if_value_is_less_than_zero(self.delay_between_cheats_in_seconds, "delay_between_cheats_in_seconds")
        self.__raise_error_if_value_is_less_than_zero(self.countdown_in_seconds, "countdown_in_seconds")

    def __raise_error_if_value_is_less_than_zero(self, value, attribute_name):
        if value < 0:
            raise ValueError(attribute_name + " must be greater than or equal to 0, but was set to " + str(value))
        