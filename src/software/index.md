# Software

## Work in progress

The software for Tanmatsu is currently under active development. On this page we will regulary post updates on our progress. Don't want to miss out on any updates? Join our Discord or Telegram groups.

### Device drivers

The invisible though crucial part of all software running on Tanmatsu. These ESP-IDF components provide  the building blocks for interfacing with the hardware on the Tanmatsu mainboard.

| Component                     | Status                 | Repository                                                                                                              |
|-------------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------|
| MIPI DSI display              | Published              | [esp32-component-mipi-dsi-abstraction](https://github.com/Nicolai-Electronics/esp32-component-mipi-dsi-abstraction)     |
| Coprocessor                   | In progress            | [esp32-component-tanmatsu-coprocessor](https://github.com/Nicolai-Electronics/esp32-component-tanmatsu-coprocessor)     |
| ES8156 audio DAC              | Published              | [esp32-component-es8156](https://github.com/Nicolai-Electronics/esp32-component-es8156)                                 |
| BMI270 IMU                    | In progress            | [esp32-component-bmi270](https://github.com/Nicolai-Electronics/esp32-component-bmi270)                                 |

#### MIPI DSI display

The Tanmatsu has a MIPI DSI display with a ST7701 controller. Espressif provides a driver for this controller, we added the correct initialization commands and configuration for the display on the Tanmatsu and packaged these in a component. In addition to the configuration of the Tanmatsu display the display included with the Espressif ESP32-P4 devkit is also supported by this component, allowing for easy switching between Tanmatsu hardware and the ESP32-P4 devkit.

#### Coprocessor

This driver component manages communication with the coprocessor firmware via I2C and exposes functions for accessing all coprocessor functionality.

#### ES8156 audio DAC

This driver component allows for configuring the ES8156 audio DAC via I2C.

#### BMI270 IMU

This driver component wraps the Bosch SDK for the BMI270 IMU, implementing communication via I2C for the ESP32-P4.

### In circuit programming

These components are as invisible during normal use as they are useful when you need them. To do initial hardware bringup and to update the firmware of the coprocessor and the radio Tanmatsu needs a way to reprogram these chips from the ESP32-P4 application processor.

| Component                     | Status                 | Repository                                                                                                              |
|-------------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------|
| RVSWD for CH32V203            | Published              | [esp32-component-rvswd](https://github.com/Nicolai-Electronics/esp32-component-rvswd)                                   |
| ESPTOOL² for ESP32-C6         | Proof of concept       |                                                                                                                         |

### Tools

The BSP (Board Support Package) wraps the driver components to provide an easy way to integrate board support for Tanmatsu (and other devices) into ESP-IDF projects.

AppFS allows for dynamically installing and running ESP32 firmware from a special flash partition. This mechanism allows for installing and running apps directly from the Tanmatsu launcher.

The LVGL BSP interface is a component providing the glue needed to use the LVGL graphics stack component provided by Espressif with the BSP component, mapping the keyboard buttons and correctly configuring the display and display rotation.

| Component                     | Status                 | Repository                                                                                                              |
|-------------------------------|------------------------|-------------------------------------------------------------------------------------------------------------------------|
| BSP                           | In progress            | [esp32-component-badge-bsp](https://github.com/badgeteam/esp32-component-badge-bsp)                                     |
| [AppFS](appfs)                | Published              | [esp32-component-appfs](https://github.com/badgeteam/esp32-component-appfs)                                             |
| LVGL BSP interface            | In progress            |                                                                                                                         |

```{toctree}
:hidden:

self
appfs/index
badgelink/index
meshtastic/index
```
