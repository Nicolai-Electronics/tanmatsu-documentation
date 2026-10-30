# Installing the template app

After you have finished compiling the Template app the next step is installing the app onto your Tanmatsu.

Your app is a full ESP32 firmware binary, meaning it can run without any of the Tanmatsu infrastructure such as the launcher. Because of this there are two directions you can take when debugging and testing your application.

Option 1 is to overwrite the launcher by flashing your app as the main firmware of the device. This of course removes the launcher and all other apps from your device, but makes debugging using JTAG easier.

Option 2 is to install your application binary to the AppFS partition using BadgeLink. By doing this your app will appear in the "Apps" menu of the launcher.

If you're used to building projects with ESP32 microcontrollers installing your firmware directly (option 1) will feel like the familiar option, as it is the same for all ESP32 based devices. However instead of directly flashing we recommend using BadgeLink instead for most situations.

## Flashing your app as primary firmware (option 1)

{{% alert title="Warning" color="warning" %}}
Following the procedure described in this section will overwrite the launcher and all other settings and apps installed on your device. You can restore the launcher using [the recovery website](https://recovery.tanmatsu.cloud).
{{% /alert %}}

For flashing your firmware three commands are available in the `Makefile` included with the template app:

- flash
- monitor
- flashmonitor

The `flash` command will flash the build output to the device using `esptool`. The `monitor` command opens the serial port monitoring tool included with ESP-IDF for viewing the log output of your application. The `flashmonitor` command does both at once, saving a couple of seconds of your time.

The `flash` and `flashmonitor` targets will automatically call the `build` target so there is no need to manually run the build target before flashing.

Just like the `build` target these make targets accept the `DEVICE` argument to set the targetted device, this defaults to `tanmatsu` but other targets like `mch2022`, `kami`, `esp32-p4-function-ev-board` and `hackaday2025` are also supported. Have a look in the Makefile to see the list of supported targets.

## Installing your app using BadgeLink (option 2)

BadgeLink is our custom USB protocol for interacting with Tanmatsu, it allows manipulating the AppFS partition, FAT partition and settings stored in the NVS partition. 
