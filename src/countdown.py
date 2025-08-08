from dataclasses import dataclass
import time

@dataclass
class Countdown:
    total_seconds: int = 10

    def __post_init__(self):
        if self.total_seconds <= 0:
            print("Total seconds must be greater than 0. The passed-in one isn't, so we're setting it to 10.")
            self.total_seconds = 10

    def start(self):
        seconds_passed = 0
        print("Ensure your game window is in focus. The inputs will be automatically typed in...")
        while seconds_passed <= self.total_seconds:
            if seconds_passed == self.total_seconds:
                print("Starting!")
                return

            print(self.total_seconds - seconds_passed)
            seconds_passed += 1
            time.sleep(1)
