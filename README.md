# PumpBot
A Discord bot made with discord.py to control the Programmable Air Arduino project.

# Instructions for Installation
Follow the instructions to get Arduino set up for your Programmable Air unit, listed on the Programmable Air GitHub. (https://github.com/Programmable-Air/Code)

Make note of the COM port that your board is listed under, you will need it to run the program.

Flash the modified FactoryFirmware.ino provided in this repository to your Programmable Air board, using the Arduino IDE.

Download the provided Python script, it should work with any Python version.

Before launching for the first time, replace TOKEN-HERE on line 46 with your dedicated Discord bot token.

Finally, use the COM number you took note of before, and set it.

# How to use the Bot
PumpBot has 3 main commands, with more potentially coming in the future. The prefix for commands is p!

The Pump command takes two arguments, the first one being the power of the pump itself. This is an integer from 0 to 100, 0 being completely off and 100 being on full power. The second argument is the duration to turn the pump on for, in seconds

Example: ```p!pump 70 20``` would turn the pump on 70 percent power, for 20 seconds.

The second command is Vent, which vents to atmosphere, this takes one argument, and vents using the release valve for the time specified, in seconds.

Example: ```p!vent 15``` would open the release valve and vent to atmosphere for 15 seconds.

The third and final (for now) command is Pressure, which sends the current pressure read by the Programmable Air unit, as well as the calibrated atmospheric pressure. There are no arguments for this command.

Example ```p!pressure``` sends the current pressure in chat, and calibrated atmospheric pressure.

![Screenshot_51](https://user-images.githubusercontent.com/112515950/187774374-b6f1aa9e-4dc8-460f-8995-c4b35aefa2bd.png)
