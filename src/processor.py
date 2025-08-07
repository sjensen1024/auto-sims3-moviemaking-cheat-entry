import definitions
import yaml

from src.configuration import Configuration

class Processor:
    def __init__(self, config_path_relative_to_project_root = 'config\\cheat_entry_config.yml'):
        self.configuration_file_path = self.__setup_configuration_file_path(config_path_relative_to_project_root)

    def run(self):
        self.configuration = Configuration(**self.__get_configuration_file_attributes())
        self.__print_configuration()

    def __setup_configuration_file_path(self, relative_path):
        return definitions.ROOT_DIR + "\\" + relative_path
    
    def __get_configuration_file_attributes(self):
        with open(self.configuration_file_path, 'r') as stream:
            config_data = yaml.safe_load(stream)
        return config_data
    
    # TODO: Remove this method, or only set it up to run with a verbose option.
    def __print_configuration(self):
        print("Configuration:")
        print("cheats_to_enter: " + ",".join(self.configuration.cheats_to_enter))
        print("delay_between_cheats_in_seconds: " + str(self.configuration.delay_between_cheats_in_seconds)) 
        print("countdown_in_seconds: " + str(self.configuration.countdown_in_seconds))
        print("should_auto_open_window: " + str(self.configuration.should_auto_open_window))
        print("window_name: " + self.configuration.window_name)
        print("should_echo_cheat_entry_in_prompt: " + str(self.configuration.should_echo_cheat_entry_in_prompt))
