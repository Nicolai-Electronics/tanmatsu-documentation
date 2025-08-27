# I2C busses on the Tanmatsu mainboard

## Internal bus

The internal I2C bus facillitates communication between the ESP32-P4 application processor and the on-board peripherals of Tanmatsu.

| Device                    | Role       | Address | Description                                                              |
|---------------------------|------------|---------|--------------------------------------------------------------------------|
| ESP32-P4                  | Controller | -       | Runs user application                                                    |
| ESP32-C6 radio            | -          | -       | I2C bus connection is not currently being used                           |
| CH32V203 coprocessor      | Peripheral | 0x5F    | Controls power management, keyboard and RTC                              |
| ES8156 audio codec        | Peripheral | 0x08    | Audio codec for the stereo audio output                                  |
| BMI270 orientation sensor | Peripheral | 0x68    | Accelerometer and gyroscope orientation sensor                           |
| Internal Add-On EEPROM    | Peripheral | 0x50    | Optional: a small EEPROM chip used to identify the attached add-on board |
| SCD4x CO2 sensor          | Peripheral | 0x62    | Optional: a carbon dioxide sensor attached to the sensor header          |

The internal add-on EEPROM resides on the add-on board and is thus only available when an add-on is attached.

The SCD4x CO2 sensor is an optional module which can be attached to the sensor header which can be soldered in by the user.

## Power management bus

The power management I2C bus allows the CH32V203 coprocessor to configure the BQ25895.

| Device                    | Role       | Address | Description                                                              |
|---------------------------|------------|---------|--------------------------------------------------------------------------|
| CH32V203 coprocessor      | Controller | -       |                                                                          |
| BQ25895 PMIC              | Peripheral | 0x6A    | Power management                                                         |

## QWIIC bus

The QWIIC connector on the Tanmatsu mainboad is connected to GPIO 33 (SDA) and GPIO 32 (SCL), allowing the user to choose between I2C (both controller and peripheral) and I3C controller modes.
There are no other devices attached to these pins, allowing the pins to be used for any purpose.

## CATT bus

The CATT connector on the Tanmatsu mainboard is connected to eight dedicated GPIO pins. Users can reconfigure each of these GPIO pins. On startup pins GPIO 12 (SDA) and GPIO 13 (SCL) are used as I2C bus.
If an EEPROM is detected at I2C address 0x50 it will be read to identify the connected add-on board.
