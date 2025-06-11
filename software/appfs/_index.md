---
title: "AppFS"
linkTitle: "AppFS"
nodateline: true
weight: 2
---

AppFS is an [ESP-IDF component](https://components.espressif.com/components/badgeteam/appfs/versions/1.0.0) that implements a method for dynamically installing and loading firmware binaries. It implements a pseudo filesystem interface for storing firmwares and a bootloader modification which allows for starting firmwares from the AppFS partition.

Originally AppFS was created by [Jeroen Domburg (sprite_tm)](https://spritesmods.com/) for the [PocketSprite](https://pocketsprite-sdk.readthedocs.io/en/latest/api/appfs.html) keychain gameconsole. Since it's creation [Badge.Team](https://badge.team) has succesfully deployed, updated and extended AppFS to make it the ready to use component it is today.

The current version of AppFS supports ESP-IDF 5.3 and later and has bootloader modifications for the ESP32, ESP32-C6 and ESP32-P4 included. Other ESP32 variants are not supported yet.

## Using the AppFS component in your projects

Apps do *not* require any changes to be started using AppFS, you only need the AppFS component to build a launcher menu.

To include the AppFS component in your launcher menu project first add the component as a requirement using idf.py:

```
idf.py add-dependency "badgeteam/appfs^1.0.0"
```

This makes the AppFS APIs available, but does not apply the required bootloader changes.

To apply the bootloader changes either create two symlinks or copy the contents of the folders.

```
mkdir bootloader_components
ln -s managed_components/badgeteam__appfs bootloader_components/appfs
ln -s managed_components/badgeteam__appfs/bootloader_main bootloader_components/main
```

The component is now ready for use.

```
#include "esp_err.h"
#include "esp_log.h"
#include "appfs.h"

void initialize_appfs(void) {
    esp_err_t res = appfsInit(APPFS_PART_TYPE, APPFS_PART_SUBTYPE);
    if (res != ESP_OK) {
        ESP_LOGE(TAG, "Failed to initialize AppFS: %s", esp_err_to_name(res));
        return;
    }
}
```

See the functions defined in [appfs.h](https://github.com/badgeteam/esp32-component-appfs/blob/main/include/appfs.h) for more information on how to use the library.

## Partition table

The `appfs.h` header defines a type and subtype for the AppFS partition:

```
#define APPFS_PART_TYPE    0x43 /*<! Default partition type of an appfs partition */
#define APPFS_PART_SUBTYPE 0x3  /*<! Default partition subtype of an appfs partition */
```

To create an AppFS partition add an entry to the partitions CSV file for your project:

```
# ESP-IDF Partition Table
# Name, Type, SubType, Offset,   Size,
appfs,  0x43, 3,       0x330000, 8000K,
```

## AppFS partition tools

After ESP-IDF has downloaded the component a `tools` folder can be found at `managed_components/badgeteam__appfs/tools`. In this folder a set of Python scripts can be found for creating and managing AppFS partition data.

### Creating an AppFS partition image

In the partition table above the partition is 8000 KB in size. Converted to bytes 8000 KB becomes `8000 x 1024 = 8192000` bytes.

A partition can be created using the following command:

```
python appfs_generate.py 8192000 example.bin
```

To add firmware binaries to the AppFS partition file the `appfs_add_file.py` tool can be used:

```
python appfs_add_file.py example.bin myapp.bin "myapp" "My app" 1
```

The name and title fields are strings. The filename (`name` field) of the file can be a maximum of 48 bytes long and the `title` of the file can be 64 bytes long. The `version` field is an 16 bits unsigned integer with a range of 0 - 65535.

The filename (`name` field) of the file is used in the AppFS API to identify files in the filesystem, filenames have to be unique. The `title` field is optional and may be used to include a human readable alternative to the filename. If unused the `title` field can be set to a blank string `""`. The `version` field is also optional and may be used to identify the installed version of an application, allowing for easier implementation of update mechanisms. If unused the `version` field can be set to `0`.

