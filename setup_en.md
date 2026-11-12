# Setup Guide For VIVIDLOPE AP

## Requirements:
- Steam version of VIVIDLOPE (full game, demo is not supported)
- Latest version of Archipelago (available [here](https://github.com/ArchipelagoMW/Archipelago/releases))
- VIVIDLOPE APWorld (available at the [releases](https://github.com/EmilyEmmi/VIVIDLOPE-AP-WORLD/releases) page)
- VIVIDLOPE AP Mod (available [here](https://github.com/EmilyEmmi/VIVIDLOPE-AP/releases))
- Delta Patcher (available [here](https://github.com/marco-calautti/DeltaPatcher/releases))

## APWorld installation

This APWorld is installed just like any other AP World. If you're unfamilar with Archipelago, I would recommend following the [Archipelago Setup Guide](https://archipelago.gg/tutorial/Archipelago/setup_en), then following the rest of these instructions:

1. Install the VIVIDLOPE APWorld by double-clicking it, or by opening the Launcher and selecting "Install APWorld".
2. In the Launcher, select Generate Template Options to get template option files for all available games. Scroll down to find VIVIDLOPE. Use this file to set up your options like any other game.
    a. Alternatively, you can use the Options Creator inside of the Archipelago Launcher.
3. Once you have the options ready, the host will need the .yaml file, as well as the VIVIDLOPE APWorld if they don't have it already. The host will host a game like usual.

## Mod installation
This only needs to be done once. It can be used to play any multiworld with VIVIDLOPE (provided the version is compatible).
1. Get the latest version of the VIVIDLOPE mod from [here](https://github.com/EmilyEmmi/VIVIDLOPE-AP/releases).
2. On Steam, select VIVIDLOPE, then click the gear icon. Go to Properties -> Game Versions & Betas, and select the "gmvm" version.
3. Select the gear icon again, then select Manage -> Browse local files. It's recommended that you copy these files elsewhere to use the mod, but you can also play the game normally even with the Archipelago mod installed.
4. Open Delta Patcher. Select VIVIDLOPE's data.win file for the original file and VIVIDLOPE-AP.xdelta for the patch. Click "Apply Patch".
5. If all goes well, you should see the message "Applied patch successfully!".

## Connecting to the Multiserver

1. Launch the modded version of VIVIDLOPE. Verify that you see "AP [version number]" on the title screen. If not, follow the instructions above to install the mod.
2. In the main menu, select the Archipelago option. Fill in the IP, port number, password (if applicable), and slot name. To change one of the values, press the Confirm button and type in the window that appears. You may need to exit full screen to see the pop-up window.
3. Once you've filled out all of the information, select "Connect". You should either load into the Pal Select menu or immediately into a save file.

## Other notes

- You can turn off Tips in the options to disable getting advice on each new stage (this is especially recommended in Stage Shuffle)
- When connecting to a multiworld, there is a new options menu labeled "AP Options". You can use this to toggle Deathlink and Deathlink amnesty at any time.
- If you disconnect from the Multiworld, pause the game and select "Reconnect" to attempt to reconnect.
- Each Multiworld you play creates a seperate save file. It's recommended that you use "Erase AP Data" every once in a while to get rid of any old save files created by the Archipelago mod.
- A QoL feature included with this mod is the ability to save your progress in Finale. Simply select "Return to Atrium" in the pause menu while playing Finale, and your progress should be restored when you re-enter the level. To restart the entire level, select "Retry". Note that losing all of your lives will also restart the level. This is intended to allow you to leave Finale in case you find yourself unable to complete a stage, not for the purposes of save-scumming. But you can use it for that purpose if you want, I don't really care.