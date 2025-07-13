# Getting started

## Introduction

Congratulations! You just got your hands on your Tanmatsu, we bet you're excited to get started so let's not delay and get right to it!

### Turning Tanmatsu on and off

The top most button on the right side of the device is the power button.

Tanmatsu has multiple power states, some are defined by software, others by hardware. Depending on the state your device is in you will need to hold down the power button for a different duration to reach the desired state.

 - If your Tanmatsu is completely turned off it is in a mode where only the clock is running. This mode requires so little power that you should not notice any battery drain in years if the device is left alone. *Pressing the power button for 2.5 seconds turns the device on* if it is in this state.
 - If your Tanmatsu is turned on *you can turn it off completely by holding down the power button for more than half a second*.
 - If you keep holding down the power button after the device has powered off then the device will *restart* 2.5 seconds after it powered off. This allows for easily rebooting your tanmatsu by holding down the power button for 3 seconds.
 - Depending on the app currently running on your Tanmatsu there might be more power states available. We recommend trying a short press of the power button to enter and leave the sleep state.

### Charging your Tanmatsu

You can charge your Tanmatsu by plugging in a power source (phone charger or computer) into the USB-C port. Tanmatsu will automatically power on when a power source is detected and battery charging will start automatically.

Tanmatsu will only charge when on or in sleep mode. *If Tanmatsu is powered off the battery will not be charged even with a power source connected to the USB-C port.* The default firmware for Tanmatsu will include a mode which turns off the radio and display and keyboard backlight before putting the ESP32-P4 application processor into deep sleep mode. You can enter this mode by pressing the power button for less than half a second. You can check if your Tanmatsu is charging by looking at the color of the power LED.

### Power LED

The color of the power LED indicates the state of the power management system.

If the power LED displays a solid single color:

 - Blue: running on battery, no charger detected
 - Yellow: charger detected, battery is being charged
 - Green: charger detected, battery is fully charged
 - Red: charger detected, no battery detected
 
If the power LED displays a blinking color:

 - Slowly blinking red: the battery is almost empty, connect a charger to avoid losing work
 - Rapidly blinking red: a fault occured in the power management circuit
 
In case you encounter a fault condition please exit the currently running app and return to the launcher menu. The launcher menu will provide more detailed information about the active fault flags.

### PMIC status LED

There is a small red LED on the back of the mainboard. This LED provides additional status information about the state of the power management system of Tanmatsu.

 - Off: the battery is not being charged
 - Slow blinking: a PMIC fault has occured
 - Rapid bliniing: Tanmatsu is trying to charge the battery but no battery is being detected
 
PMIC stands for "Power Management Integrated Circuit". Tanmatsu uses a BQ25895 PMIC from Texas Instruments to manage battery charging.

### Fault conditions

A fault doesn't immediately mean there is anything wrong with your Tanmatsu and using a Lithium Polymer battery is not dangerous if the battery is handled correctly. Tanmatsu contains a multiple layers of protection to prevent any damage to your device, the battery or it's surroundings. If charging is stopped due to a fault then most likely there is something wrong with your battery, though this doesn't immediately have to be a problem.

The protection functions built into the Tanmatsu mainboard will, in addition to the battery protection circuit built into the battery itself, stop charging if it detects that the battery voltage is below the minimum safe threshold for a Lithium Polymer battery or above the maximum voltage threshold of a Lithium Polymer battery. In both cases the power LED will rapidly blink in red and the small red LED on the back of the mainboard will 

A situation that can trigger the under-voltage protection is a situation where the battery has drained below it's rated minimum voltage due to degradation when left completely empty for a long period of time. In this situation is is also possible that the battery simply is not detected, in which case the power LED will turn red when an external power source is connected. If the battery has accidently reached a voltage near 2.5 volt then the battery will be disconnected to protect it. Normally the battery voltage recovers a bit automatically after leaving the battery alone for a few minutes. In this situation you can safely restart start charging the battery again after the voltage has reached it's normal level.

The battery supplied with your Tanmatsu has a built-in protection circuit preventing the battery from draining below it's minimum rated voltage during normal use.

A Lithium Polymer battery that has reached a voltage below 2.5 volt for a prolonged period of time can become chemically unstable, we recommend replacing the battery if your battery has drained below 2.5 volt. Recharging a Lithium Polymer battery that has been subjected to a situation where it reached a voltage of less than 2.5 volt can be dangerous, the battery may for example swell up and could potentially damage the device or it's surroundings.

#### Debug connection

To connect to the USB debug, use the monitor function from ESP-IDF. Remember to have the USB function in debug mode.

The flow is as following:
* Set the USB in USB mode
* Compile the app
* Upload the app using bagdelink
* Set the USB to debug mode (such that the small bug is visible)
* Run the following command in your app folder to monitor the app:

```bash
PORT=/dev/cu.usbmodem1301 make monitor
```

Change PORT to match what device name your Tanmatsu gets when you connect it to your computer. cu.usbmodem1301 is for Mac OS.

Monitor function automatically decode stacktraces.

You might need to kill the monitor process to quit the monitor function. At least for Mac OS.

```{toctree}
:hidden:

self
compiling_the_template_app/index
```
