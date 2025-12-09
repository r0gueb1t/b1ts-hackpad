import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys  # media keys support [web:29]

keyboard = KMKKeyboard()

# --- modules / extensions ---
macros = Macros()
keyboard.modules.append(macros)
keyboard.extensions.append(MediaKeys())

# --- pins ---
# 4 normal macro keys
MACRO_PINS = [board.D1, board.D2, board.D3, board.D4]
# EC11 encoder: B, A, SW (your mapping)
ENC_PINS = [board.D8, board.D9, board.D11]

PINS = MACRO_PINS + ENC_PINS  # total 7 "keys"

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Index in keymap matches PINS:
#   0 -> D1  (macro 1)
#   1 -> D2  (macro 2)
#   2 -> D3  (macro 3)
#   3 -> D4  (macro 4)
#   4 -> D8  (encoder B)
#   5 -> D9  (encoder A)
#   6 -> D11 (encoder switch)
keyboard.keymap = [
    [
        # 4 macro keys (change these to whatever you want)
        KC.MACRO("Macro 1!"),  # D1
        KC.MACRO("Macro 2!"),  # D2
        KC.MACRO("Macro 3!"),  # D3
        KC.MACRO("Macro 4!"),  # D4

        # encoder pins as media keys
        KC.VOLD,               # D8 (one direction) volume down
        KC.VOLU,               # D9 (other direction) volume up
        KC.MUTE,               # D11 push to mute/unmute
    ]
]

if __name__ == '__main__':
    keyboard.go()
