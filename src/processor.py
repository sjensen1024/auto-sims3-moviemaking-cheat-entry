import definitions
import yaml
from src.configuration import Configuration
from src.cheat_entry import CheatEntry
from src.game_window import GameWindow
from src.countdown import Countdown

class Processor:
    def __init__(self, config_path_relative_to_project_root = 'config\\cheat_entry_config.yml'):
        self.configuration_file_path = self.__setup_configuration_file_path(config_path_relative_to_project_root)

    def run(self):
        self.configuration = Configuration(**self.__get_configuration_file_attributes())
        self.cheat_entry = CheatEntry(delay_between_cheats_in_seconds=self.configuration.delay_between_cheats_in_seconds)
        self.countdown = Countdown(total_seconds=self.configuration.countdown_in_seconds)
        if self.configuration.should_auto_open_window:
            self.game_window = GameWindow(window_name=self.configuration.window_name)
            self.game_window.bring_window_to_front()
        self.countdown.start()
        for cheat in self.configuration.cheats_to_enter:
            self.cheat_entry.enter_cheat(cheat)
        print("Done!")

    def __setup_configuration_file_path(self, relative_path):
        return definitions.ROOT_DIR + "\\" + relative_path
    
    def __get_configuration_file_attributes(self):
        with open(self.configuration_file_path, 'r') as stream:
            config_data = yaml.safe_load(stream)
        return config_data
