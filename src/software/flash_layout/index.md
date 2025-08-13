<img width="85" height="17" alt="image" src="https://github.com/user-attachments/assets/048f4440-54fa-4ddb-8a19-298efb55bf99" /># ESP32-P4 flash layout

The ESP32-P4 application processor has a 16MB flash chip attached to it for storing firmware, applications and files.

## Manually flashing the launcher firmware using esptool

Download the latest [release](https://github.com/Nicolai-Electronics/tanmatsu-launcher/releases) from the launcher firmware repository. For Tanmatsu you need the `tanmatsu.zip` package attached to the release.

This zip archive contains `.bin` and `.elf` files.

The `.elf` files are the full unstripped loadable application files with debug symbols. You only need those for debugging, for example to parse backtraces into human readable data.

The `.bin` files only contain the required parts and have been rearranged to allow execution of the application. You can flash these files to the flash chip of the ESP32-P4 using `esptool`.

| Filename              | Description                  | Flash address |
|-----------------------|------------------------------|---------------|
| bootloader.bin        | Second stage bootloader      | 0x002000      |
| partition-table.bin   | Partition table              | 0x008000      |
| ota_data_initial.bin  | A/B firmware selection reset | 0x01d000      |
| tanmatsu-launcher.bin | Firmware                     | 0x020000      |
| locfd.bin             | FAT filesystem               | 0xc20000      |

To flash these files using `esptool.py` you can use the following command:

```
python -m esptool --chip esp32p4 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 16MB --flash_freq 80m 0x2000 bootloader.bin 0x8000 partition-table.bin 0x1d000 ota_data_initial.bin 0x20000 tanmatsu-launcher.bin 0xc20000 locfd.bin
```

Note that this will erase the files on the FAT partition of your Tanmatsu. If you only wish to reinstall the firmware you can run the following command, provided that the FAT partition in flash is already valid:

```
python -m esptool --chip esp32p4 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_size 16MB --flash_freq 80m 0x2000 bootloader.bin 0x8000 partition-table.bin 0x1d000 ota_data_initial.bin 0x20000 tanmatsu-launcher.bin
```

## Detailed flash layout

The stock configuration of partitions on Tanmatsu is as follows:

| Region start | Region end | Size                 | Description                    |
|--------------|------------|----------------------|--------------------------------|
| 0x0          | 0x1FFF     | 8 KB (2 sectors)     | *Unused*                       |
| 0x2000       | 0x7FFF     | 24 KB (6 sectors)    | Second stage bootloader        |
| 0x8000       | 0x8FFF     | 4 KB (1 sector)      | Partition table                |
| 0x9000       | 0x18FFF    | 64 KB (16 sectors)   | *Unused*                       |
| 0x19000      | 0x1CFFF    | 16 KB (4 sectors)    | Non-volatile storage           |
| 0x1d000      | 0x1FFFF    | 12 KB (3 sectors)    | OTA data                       |
| 0x20000      | 0x21FFFF   | 2 MB (512 sectors)   | Firmware partition A           |
| 0x220000     | 0x41FFFF   | 2 MB (512 sectors)   | Firmware partition B           |
| 0x420000     | 0xC1FFFF   | 8 MB (2048 sectors)  | Application filesystem         |
| 0xc20000     | 0xFFFFFF   | 3.9 MB (992 sectors) | FAT filesystem                 |

Notes:

 - The unused section at the start of flash is used when secure boot is enabled, secure boot is permanently disabled on Tanmatsu to prevent accidental bricking
 - Second stage bootloader offset (0x2000) is fixed because the first stage (ROM) bootloader always loads from this address
