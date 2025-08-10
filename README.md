# Automatic Sims 3 Moviemaking Cheat Entry
This is a YAML-configurable Python program
that will automatically enter common moviemaking cheat codes
into your Sims 3 game.

# Installation
- Clone this repository.
- Go to the root directory of the project and run `pip install -r requirements.txt`.

# Configuration in config/cheat_entry_config.yml
### The following settings can be configured in your project's config/cheat_entry_config.yml
- `delay_between_cheats_in_seconds` tells the program
  how many seconds it should pause between entering each cheat. The default value is 0.25.
- `countdown_in_seconds` tells the program
  how many seconds to wait for your window to open - 
  or for you to open the window if it's set up to 
  not automatically open the window or if it can't find it -
  before trying to enter the cheats.
  The default value is 10.
- `should_auto_open_window` tells the program
  whether it should try to automatically bring
  your Sims 3 game to the front. If true, it will do that.
  If false, it won't even try to do that and will expect
  you to do it yourself. The default value is true.
- `window_name` is a case-insensitive way to tell the program
  what window to look for if you've configured it
  to try to auto-open your Sims 3 game's window.
  It will try to find the first window including the specified text.
  Its default value is "the sims 3".
- `cheats_to_enter` tells the program what cheats to enter.
  It defaults to the following, but you can add whatever you want as long as you follow the correct YAML format:
  - moveObjects on
  - disableSnappingToSlotsOnAlt on
  - testingCheatsEnabled true
  - movieMakerCheatsEnabled true
  - hideHeadlineEffects on
  - fadeObjects off
  - BuyDebug true

# Usage
### How to run the program
- Open your Sims 3 game and go into gameplay mode.
- Put the game into the background (window key will do this).
- Ensure there is an input file for your project to read from (see configuration above).
- Navigate to the root project directory in a command prompt and run `python .`
