# ESP-IDF from scratch

ESP-IDF is can be a bit of a moving target at times, because of this we recommend not using one system wide installation but one per project. By doing this you can avoid compatibility problems between the ESP-IDF version and your projects.

This document describes how to start a new ESP-IDF project with ESP-IDF installed on a per-project basis.

## Requirements

 - A computer with a Linux distro or a Debian/Ubuntu WSL2 environment installed
 - Git should be installed (`sudo apt-get install git`)

## Create a project folder

Create a new folder in a place you can access, make sure there are no spaces in any part of the path.

## Download ESP-IDF

Find the [release of ESP-IDF](https://github.com/espressif/esp-idf/releases/) you want to use and inside of your new project folder execute the `git clone` command detailed in the release notes.

For ESP-IDF version 5.5 the `git clone` command is:

```
git clone -b v5.5 --recursive https://github.com/espressif/esp-idf.git esp-idf-v5.5
```

## Installing ESP-IDF

First you want to set two environment variables, `IDF_PATH` to set the path at which the ESP-IDF SDK is located and `IDF_TOOLS_PATH` to set the path to which ESP-IDF installs the toolchain files.

You can do this by creating a new text file, name it for example `env`. Open it with your text editor and store the following commands into the file:

```
#!/usr/bin/env bash
export IDF_PATH="$PWD/esp-idf-v5.5"
export IDF_TOOLS_PATH="$IDF_PATH-tools"
```

After storing this file run `source env` to activate the environment variables in your current shell. You have to do this every time you open a new shell and want to start working on the project.

In the shell in which you have sourced the environment file run the install command from the ESP-IDF folder:

```
./esp-idf-v5.5/install.sh
```

This should automatically create the `esp-idf-v5.5-tools` folder in your project directory. The installation process will end with a message reading

```
All done! You can now run:

  . ./esp-idf-v5.5/export.sh
```

Ignore those instructions, instead you will need to extend the `env` file with the environment included with ESP-IDF. For that extend the `env` file as follows:

```
#!/usr/bin/env bash
export IDF_PATH="$PWD/esp-idf-v5.5"
export IDF_TOOLS_PATH="$IDF_PATH-tools"
source "$IDF_PATH/export.sh"
```

Now source your environment again by running `source env` once more.

The command output should end with:

```
Done! You can now compile ESP-IDF projects.
Go to the project directory and run:

  idf.py build
```

This means ESP-IDF is now ready for use.

## Creating a project

Run `idf.py create-project hello_world` in which `hello_world` is the name of your new project.

## Switching to a different ESP32 variant

By default the ESP-IDF SDK targets the original `ESP32`. If you for example want to target the `ESP32-P4` you can do so by running:

```
idf.py set-target esp32p4
```

## Building your project

To build the project simply run:

```
idf.py build
```

## Flashing your project

To overwrite the firmware of an ESP32 board with your new project you can either run the `esptool.py` command presented by ESP-IDF in the build output or you can run:

```
idf.py flash --port /dev/ttyACM0
```

In which `/dev/ttyACM0` is the target serial port. On Windows this would be a `COM` port such as `COM5`, you can find out using the Windows `Device Manager`.


## Viewing debug output

ESP-IDF includes a monitor tool which automatically converts printed addresses into filename and line information.

You can start the monitor using:

```
idf.py monitor --port /dev/ttyACM0
```

You can also build, flash and start the monitor in one command:

```
idf.py build flash monitor --port /dev/ttyACM0
```

To exit out of the monitor press `CTRL+]`.

## Making your app print hello world

The entry point of your app is the `app_main()` function in `main/hello_world.c`.

Open that file and as `#include <stdio.h>` is already present you can simply add `printf("Hello world!\r\n");` to the main function to output `Hello world!` into the monitor.

Simply run the flash and monitor command (`idf.py build flash monitor --port /dev/ttyACM0`) again to rebuild and flash your app. The monitor should start automatically after your app is compiled and flashed successfully and it should print `Hello world!` (after some logging of the boot process).

## Installing the board support package for Badge.Team badges and Nicolai Electronics Tanmatsu

Exit out of the monitor (`CTRL+]`). Then add the `badge-bsp` component using the command:

```
idf.py add-dependency "badgeteam/badge-bsp^0.3.0" 
```

Also take a look at [components.espressif.com](https://components.espressif.com/) for more fun libraries you can use in your projects.

After adding the `badge-bsp` component to your project you can use the BSP to initialize the peripherals of the board. To do that add the `#include "bsp/device.h"` header to your `hello_world.c` file and run `bsp_device_initialize();` in your `app_main()` function.

Your `hello_world.c` will look like this:

```
#include <stdio.h>
#include "bsp/device.h"

void app_main(void)
{
    bsp_device_initialize();
    printf("Hello world!\r\n");
}

```

Currently the `badge-bsp` component requires that the `RTC retained memory` has a user section. This is not enabled by default. To enable this feature of ESP-IDF run:

```
idf.py menuconfig
```

Using the menuconfig screen you can change the configuration of the SDK. In this case navigate to `Bootloader config --->` and select the `Reserve RTC FAST memory for custom purposes` option. Then set the `Size in bytes for custom purposes` option to `0x100`.

For ESP32-P4 projects enabling the `experimental` high speed PSRAM feature is a must. On Tanmatsu your app will not have enough memory for the framebuffer otherwise. If you were to run your app as-is it would crash with the following error:

```
E (230) lcd.dsi.dpi: esp_lcd_new_panel_dpi(226): no memory for frame buffer
E (230) st7701_mipi: esp_lcd_new_panel_st7701_mipi(103): create MIPI DPI panel failed
```

To enable PSRAM go back to the main menu of the menuconfig screen (`ESC`) and select the `Make experimental features visible` option. Then go to `Component config --->`, followed by `ESP PSRAM --->`. Select the `Support for external PSRAM` option and enter the new `PSRAM config --->` menu that appears. Enter the `Set PSRAM clock speed (20MHz clock speed)  --->` menu and select the `200MHz clock speed` option.

Press `q` to quit, then press `y` to save.

Now run `idf.py build flash monitor --port /dev/ttyACM0` again to build, flash and monitor the app.

You are now ready to start using the project you created to do awesome things. More information about `badge-bsp` will soon be published.
