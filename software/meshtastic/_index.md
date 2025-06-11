---
title: "Meshtastic"
linkTitle: "Meshtastic"
nodateline: true
weight: 3
---

This document describes how to install Meshtastic compatible firmware onto your Tanmatsu. The Meshtastic firmware for Tanmatsu is in active development and not yet fully stable. You might experience crashes and bugs.

Tanmatsu uses two ESP32 chips, one as application processor and one as radio. The GUI app for Meshtastic, running on the application processor can be installed as an app using BadgeLink. Support for installing applications in a similar fashion on the radio is still being worked on. Because of this it is currently required to replace the radio firmware which provides the launcher and apps on the application processor with WiFi and BLE access when installing Meshtastic onto the radio.

A tool for flashing Meshtastic or the default "ESP-HOSTED" firmware to the radio will soon be provided as a web application making use of Webserial to connect to your Tanmatsu. It is also possible to flash firmware to the radio using esptool.py, the flashing script provided by Espressif. This guide explains how to flash Meshtastic using esptool.py, which is assumed to be installed and available on your system.

{{% alert title="Stability" color="warning" %}}
This software is not stable yet, you will experience crashes, mostly of the GUI software. We hope to resolve these issues soon but keep this in mind when you install the app.
{{% /alert %}}

{{% alert title="BLE" color="warning" %}}
BLE does not work properly due to a bug in the Meshtastic radio firmware. You can connect to the radio using the official Meshtastic frontend apps in the webbrowser and on your phone over USB and WiFi without issues. This is a software bug in the Meshtastic firmware on all ESP32-C6 targets which we hope gets resolved soon.
{{% /alert %}}

## Requirements

 - [Package containing builds of the Meshtastic radio firmware and GUI application](tanmatsu-meshtastic-preview.zip)
 - [BadgeLink tools](https://github.com/badgeteam/esp32-component-badgelink/releases/download/v0.0.2/tools.zip)
 - [Esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32/installation.html)
 
Download the two archives linked to above and extract them to a folder. Then open a command prompt in that same folder.

## Installing the radio firmware

The first step is to replace the ESP-HOSTED radio firmware normally running on the ESP32-C6 with the Meshtastic firmware.

### Controlling the state of the radio using the launcher firmware

If the launcher is unable to communicate with the radio via the protocol implemented by ESP-HOSTED the launcher will automatically power off the radio. You can see the state of the radio by looking at the color of the radio LED, which is the middle LED on the left side of the front of Tanmatsu. If the LED is green the radio is powered on and working, if the LED is blue the radio is in bootloader mode and if the LED is off then the radio is powered off.

While on the homescreen of the launcher firmware you can press a key combination to force the radio into either of the three states (off, bootloader and on).

| Key combination      | Radio state | LED color |
|----------------------|-------------|-----------|
| Fn + red X           | Off         | Off       |
| Fn + orange triangle | Bootloader  | Blue      |
| Fn + yellow square   | On          | Green     |

The radio can be flashed using the online recovery tool or using esptool.py via the USB interface exposed by the radio when the radio is in either bootloader or on state. Sometimes the firmware on the radio can cause issues when trying to flash, in such a situation it is useful to try flashing while in bootloader mode. The bootloader is located in read-only memory and will always work, regardless of the state of the installed firmware.

### Flashing firmware to the radio using esptool.py

Both the application processor and the radio expose a serial port for debugging and flashing when enabled. The first serial port to appear is the ESP32-P4 application processor and the second serial port is the ESP32-C6 radio.

You can install the Meshtastic firmware by first erasing and then overwriting the firmware on the ESP32-C6 radio using the following commands:

```
esptool.py --chip esp32c6 erase_flash
esptool.py --chip esp32c6 write_flash 0x0 radio/bootloader.bin 0x10000 radio/firmware.bin 0x8000 radio/partitions.bin
```

## Installing the GUI app

Now that the radio is running Meshtastic the GUI app can be used to interact with the Meshtastic firmware running on the radio.

### Switching the USB mode of the ESP32-P4 to BadgeLink mode

Press the purple diamond button while on the homescreen of the launcher firmware. The bug icon in the top right corner of the screen should now be replaced with an USB icon. In BadgeLink mode the application processor exposes an interface which allows for installing applications. You can use this interface using the BadgeLink tools.

### Installing the Meshtastic app

Installing the Meshtastic GUI is done using BadgeLink.

Run the following command to install the Meshtastic GUI application:

```
./badgelink.sh appfs upload meshtastic "Meshtastic" 0 meshtastic-gui.bin
```

