import pynput
import time
import os
import yaml
import io

from pynput.keyboard import Key, Controller

def run():
    process_args = setup_process_args()
    begin_countdown(process_args)
    process_cheats(process_args)
    print("Done!")


def begin_countdown(process_args):
    countdown_in_seconds = process_args.get('countdown_in_seconds')
    if countdown_in_seconds <= 0:
        countdown_in_seconds = 10

    seconds_passed = 0
    print("Open your Sims 3 game window now. The inputs will be automatically typed in...")
    while seconds_passed <= countdown_in_seconds:
        if seconds_passed == countdown_in_seconds:
            print("Starting!")
            return

        print(countdown_in_seconds - seconds_passed);
        seconds_passed += 1
        time.sleep(1)

def setup_process_args():
    input_controller = Controller()
    config_data = get_config_data()
    return {
      'input_controller': input_controller,
      'cheats_to_enter': config_data.get('cheats_to_enter'),
      'cheat_entry_delay_in_seconds': config_data.get('cheat_entry_delay_in_seconds'),
      'should_echo_cheat_entry_in_cmd': config_data.get('should_echo_cheat_entry_in_cmd'),
      'countdown_in_seconds': config_data.get('countdown_in_seconds')
    } 

def get_config_data():
    with open("./cheat_entry_config.yml", 'r') as stream:
        config_data = yaml.safe_load(stream)
    return config_data

def process_cheats(process_args):
    cheats = process_args.get('cheats_to_enter')
    should_echo_cheat_entry_in_cmd = process_args.get('should_echo_cheat_entry_in_cmd')
    for cheat in cheats:
        process_cheat(cheat, process_args)
        if should_echo_cheat_entry_in_cmd:
            print(f"Cheat processed: {cheat}")

def process_cheat(cheat, process_args):
    keyboard = process_args.get('input_controller')
    open_cheat_prompt(keyboard)
    delay_in_seconds = get_cheat_entry_delay_in_seconds(process_args)
    time.sleep(delay_in_seconds)
    keyboard.type(cheat)
    time.sleep(delay_in_seconds)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(delay_in_seconds)

def get_cheat_entry_delay_in_seconds(process_args):
    cheat_entry_delay_in_seconds = process_args.get('cheat_entry_delay_in_seconds')
    if cheat_entry_delay_in_seconds <= 0:
        cheat_entry_delay_in_seconds = 1

    return cheat_entry_delay_in_seconds    


def open_cheat_prompt(keyboard):
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)

run()
