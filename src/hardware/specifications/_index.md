---
title: "Tanmatsu: specifications"
linkTitle: "Specifications"
nodateline: true
weight: 1
---

This section lists the technical specifications of the Tanmatsu hardware.

_Note: information on this page is actively being worked on and might contain accidental errors and inaccuracies._

## Physical dimensions

Size of the device including the 3D printed case:

 - Width: 12 cm (4.72 in)
 - Length: 13.5 cm (5.31 in)
 - Height: 1.8 cm (0.71 in)

Weight: 215 g (0.47 pounds) including case and battery

## Case

See [case](../case).

## Peripherals

### Display

 - Model: [SWI](http://www.swicn.com/) LH397K-IC01
 - Size: 3.97 in diagonally, 51.84 x 86.40 mm
 - Resolution: 480x800
 - Colors: 65536 colors (16-bit / RGB565)
 - Controller: ST7701S
 - Interface: MIPI DSI (2 lanes)
 - Brightness: 330cd/m2

Note: display supports 16M colors (24-bit / RGB888) but current software can not make use of this mode.

Nicolai Electronics developed an [ESP-IDF component](https://components.espressif.com/components/nicolaielectronics/mipi_dsi_abstraction) for configuring the MIPI DSI peripheral in the ESP32-P4 for use with this display.
The component also allows for easy switching between the display on the Tanmatsu and the display included with the official ESP32-P4 development kit.

The display will be available as a spare part from our webshop once Tanmatsu is shipped.

### Keyboard

 - Full 69-key alphanumeric keyboard with colored 6 function keys
 - Metal dome sheet for tactile feeling
 - LED backlight (white)

The keyboard has been developed by our awesome friends at [Solder Party](https://www.solder.party/).

The keyboard and corresponding metal dome sheet will be available as a spare part in our webshop once Tanmatsu starts shipping.

### Battery

Single cell protected Lithium Polymer battery with PH-2.0 style connector.
The connector and pinout are compatible with the battery connector on Adafruit boards.

| Parameter                | Value                                  |
|--------------------------|----------------------------------------|
| Capacity                 | 2500 mAh                               |
| Nominal voltage          | 3.7 V                                  |
| Chemistry                | Lithium Polymer                        |
| Dimensions               | "104050" (w: 10mm, h: 40mm, l: *52mm*) |
| Connector                | JST compatible PH 2.0                  |
| Manufacturer             | Tewaycell                              |
| Minimum cell voltage [V] | 2.5v (3.0v recommended)                |
| Nominal cell voltage [V] | 3.7 V                                  |
| Maximum cell voltage [V] | 4.2 V                                  |

The battery will be available as a spare part in our webshop once Tanmatsu starts shipping.

## Connectors and interfaces

On the outside of the case:
 - USB-C device port connected to an USB hub. Allows access to:
   * The ESP32-P4 USB interface (PHY 1, defaults to USB-serial/JTAG debug interface but can be remapped to custom USB functions by software)
   * ESP32-C6 USB-serial/JTAG debug interface
   * Personality module expansion port (provides access to an optionally connected USB device on a personality module)
 - USB-A host port (480 Mbit superspeed USB 2.0), provides 1A of current with automatic current limiting
 - Qwiic and Stemma-QT compatible 4-pin SH connector for connecting I2C and I3C accessories
 - 3.5 mm headphone jack
 - CATT (Connect All The Things) connector: combined PMOD and SAO compatible 2.54 mm pinsocket optionally also usable as JTAG interface for debugging the ESP32-P4 application processor
 - Three push buttons (Power, up and down). Holding down the down button when applying power puts the ESP32-P4 into USB download mode for easy firmware recovery
 - Micro SD card slot compatible with SDIO 2 and SDIO 3 cards at 3.3v and 1.8v voltage levels
 - (optional) SMA antenna connector for LoRa antenna

On the inside of the case:
 - PH-2.0 2-pin battery connector
 - PicoBlade 2-pin speaker connector for 8 Ohm speaker
 - Raspberry Pi camera compatible 22-pin MIPI CSI camera interface
 - IPEX-1 antenna connector for LoRa antenna
 - Personality module connector: 36-pin 2.54 mm pinsocket with:
   * Access to power rails (5V, Vbatt, Vsys and 3.3v)
   * USB hub downstream port connected to the USB-C port via an USB hub
   * Internal I2C bus (can be used for sensors and for an identification EEPROM)
   * 14 GPIO pins
   * ESP32-P4 USB interface (PHY 2) or 2 extra GPIO pins
   * UART interface or 2 extra GPIO pins
   * I2S interface or 4 extra GPIO pins (shared with audio codec, when used as GPIO audio functionality is unavailable)
   * I3C bus (shared with 4-pin SH connector) or 2 extra GPIO pins

## Chips and modules

### WiFi, BLE and IEEE 802.15.4 radio

Module: Espressif Systems ESP32-C6-WROOM-1-N8

 - CPU: 32-bit RISC-V single core microprocessor, up to 160 MHz
 - RAM: 512 KB
 - WiFi: WiFi 6 on 2.4GHz
 - BLE: 5.3
 - Mesh networking: IEEE 802.15.4-2015 protocol, supports Thread 1.3 and Zigbee 3.0
 - Flash: 8 MB

More information can be found in the [Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c6-wroom-1_wroom-1u_datasheet_en.pdf).

### Application processor

Chip: Espressif Systems ESP32-P4NRW32

 - CPU: 32-bit RISC-V dual core microprocessor, up to 400 MHz
 - RAM: 32 MB
 - Flash: 16 MB

The datasheet for this chip is not yet publicly available

### Management coprocessor

Chip: WCH CH32V203C8T6

 - CPU: 32-bit RISC-V single core microprocessor, up to 144 MHz
 - RAM: 20KB
 - Flash: 64 KB

More information can be found in the [Datasheet](https://www.wch-ic.com/downloads/CH32V203DS0_PDF.html).

The management coprocessor is responsible for reading the keyboard matrix and power management. It presents itself as an I2C peripheral on the internal I2C bus of the Tanmatsu and provides the following services:

 - Keyboard events
 - PWM control for the display backlight
 - PWM control for the keyboard backlight
 - Real Time Clock (RTC) backed by watch crystal
 - Alarm wakeup
 - PMIC control
 - Power switching for USB-A port
 - Power and boot-mode control for the ESP32-C6 radio module
 - Power switching for audio amplifier
 - Headphone detection
 - Addressable LED control for the 6 built-in addressable LEDs

The firmware for this chip will be made available under terms of the MIT license after the product starts shipping to customers. Modifying the firmware is of course possible but is not recommended.

The firmware of the coprocessor can be updated from the ESP32-P4 application processor, for this Nicolai Electronics developed an [ESP-IDF component](https://components.espressif.com/components/nicolaielectronics/rvswd) capable of reprogramming CH32V20x and CH32V30x microcontrollers from the ESP32-P4 application processor.

### LoRa radio

The PCB footprint supports a range of radio modules from [Ai-Thinker](https://ai-thinker.eu/). Software support will initially be provided for the [RA-01SH](https://docs.ai-thinker.com/_media/lora/docs/ra-01sh_specification.pdf) 868 MHz band [SX1262](https://www.semtech.com/products/wireless-rf/lora-connect/sx1262) based and the RA-01S 433 MHz band [SX1268](https://www.semtech.com/products/wireless-rf/lora-connect/sx1268) based modules.

All Tanmatsu boards will be delivered with a module which has the IPEX-1 antenna connector installed. Optionally an SMA antenna connector can be installed to allow connecting standard external LoRa antennas. Tanmatsu will be provided with either an internal IPEX-1 antenna or a basic SMA antenna depending on the option chosen.

### Audio

Everest Semiconductor ES8156 audio codec:
 - Hardware volume control via I2C interface
 - Stereo audio DAC

FM8002A mono speaker amplifier:
 - Can be switched on and off using the coprocessor
 - Connected to built-in 8 Ohm speaker

### Power management

#### PMIC

Texas Instruments BQ25895RTW PMIC for battery charging and monitoring as well as DC/DC boost converter for 5 volt rail (to power USB-A port, addressable LEDs and 5 volt pin on the personality module expansion header).

Provides soft power on/off functionality when the device is battery powered and allows seamless transition between battery and USB-C power source.

#### 3.3v rail DC/DC converter

Texas Instruments TPS63020DSJR DC/DC buck and boost converter providing a stable 3.3v rail even when the battery voltage drops below 3.3 volt.

#### Backlight drivers

Two AP3032KTR backlight driver chips, one for the display and one for the keyboard backlight LEDs.
Brightness controlled using PWM via the CH32V203 coprocessor.

#### Standby power rail

A small LDO provides 2.5v to the Vbatt rail of the CH32V203 coprocessor even when the device is off. This uses almost no power (theoretically the battery would last over 10 years on a single charge if the device is never turned on, ignoring LiPo battery self-discharge) and allows the Real Time Clock in the CH32V203 coprocessor to keep track of time even when the device is off. A special latch circuit circuit allows the CH32V203 to power on the Tanmatsu using its alarm pulse output by emulating a press of the power button.

### Addressable LEDs

Six SK6805-EC20 addressable LEDs controlled by the coprocessor.

### Sensors

 - Bosch BMI270 IMU combined accelerometer and gyroscope
 - Header for optional SCD40 or SCD41 CO2, temperature and humidity sensor (not populated, modules are available on AliExpress) or other I2C controlled sensor

## Questions?

If you have questions please contact us by joining one of our community chatgroups ([Telegram](https://t.me/+SueEz5IWYR05NzU8) and [Discord](https://discord.gg/KkY6JqNCqT)) or by [emailing](mailto:contact@nicolaielectronics.nl) us.

