# Keyboard

Tanmatsu has a built-in QWERTY keyboard. Besides the letter, number and symbol
keys it carries a row of colored function keys and an **AltGr** layer that
gives direct access to accented letters and common symbols.

The keyboard matrix is scanned by the CH32V203 coprocessor; the ESP32-P4
receives decoded key events through the
[badge BSP](https://github.com/badgeteam/esp32-component-badge-bsp/blob/main/targets/tanmatsu/badge_bsp_input.c).
Each key event provides an ASCII byte, a UTF-8 string (already resolved for the
active modifier layer) and a modifier bitmask.

## Function keys

The colored keys along the top row are the navigation / function keys
(`BSP_INPUT_NAVIGATION_KEY_F1`…`F6`). Their meaning is defined by the running
application.

| Symbol | Color   | Event |
|--------|---------|-------|
| ✕      | red     | `F1`  |
| △     | orange  | `F2`  |
| ☐      | yellow  | `F3`  |
| ◯     | green   | `F4`  |
| ☁      | blue    | `F5`  |
| ◇     | magenta | `F6`  |

Applications reuse the same colored keys for their own actions — a chat app
might put an emoji picker on the green ◯ and a special-character picker on the
blue ☁, for instance.

## AltGr layer

Hold **AltGr** and press a key to enter an accented letter or symbol directly.
The default layout maps as follows (AltGr / AltGr+Shift):

### Letters

| Key | AltGr | +Shift | | Key | AltGr | +Shift |
|---|---|---|---|---|---|---|
| Q | ä | Ä | | A | á | Á |
| W | å | Å | | S | ß | § |
| E | é | É | | D | ð | Ð |
| R | ® | ™ | | F | ë | Ë |
| T | þ | Þ | | J | ï | Ï |
| Y | ü | Ü | | K | œ | Œ |
| U | ú | Ú | | L | ø | |
| I | í | Í | | Z | æ | Æ |
| O | ó | Ó | | X | · | |
| P | ö | Ö | | C | © | ¢ |
| | | | | N | ñ | Ñ |
| | | | | M | µ | ± |

### Numbers and symbols

| Key | AltGr | | Key | AltGr |
|---|---|---|---|---|
| 1 | ¡ | | 8 | ¾ |
| 2 | ² | | 9 | ‘ |
| 3 | ³ | | 0 | ’ |
| 4 | ¤ | | - | ¥ |
| 5 | € | | [ | « |
| 6 | ¼ | | ] | » |
| 7 | ½ | | / | ¿ |
|   |   | | \ | ¬ |

Several keys (`= ; ' , .` and the shifted number row) carry **combining
diacritical marks** on the AltGr layer, which combine with the next character
rather than printing standalone.

The authoritative layout is the keymap table in
[`badge_bsp_input.c`](https://github.com/badgeteam/esp32-component-badge-bsp/blob/main/targets/tanmatsu/badge_bsp_input.c#L352).
Whether a given character is displayed depends on the running application's font
coverage.

The keyboard layout is based on the `US international with Alt Gr` keyboard layout.
