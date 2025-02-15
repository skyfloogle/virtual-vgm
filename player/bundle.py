#!/usr/bin/env python

import argparse
from pathlib import Path
import sys


def make_rom(out_fn, in_fns):
    data = len(in_fns).to_bytes(2, 'little')
    for fn in in_fns:
        data += Path(fn).stem.encode('ascii', 'replace') + b'\0'
    data += b'\0' * (-len(data) % 4)
    for fn in in_fns:
        with open(fn, "rb") as f:
            data += f.read()
            data += b'\0' * (-len(data) % 4)

    with open(Path(sys.argv[0]).parent / "player.bin", "rb") as f:
        while (ch := f.read(2)) == b'\xbf\xbf': pass
        player = ch + f.read()

    total = len(data) + len(player)
    padding = (1 << (total - 1).bit_length()) - total

    with open(out_fn, "wb") as f:
        f.write(data)
        f.write(b'\0' * padding)
        f.write(player)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Virtual Boy ROM that plays the given VGM files.")
    parser.add_argument("rom", help="The ROM to create.")
    parser.add_argument("vgm", nargs="+", help="One or more .vgm files.")

    args = parser.parse_args()
    make_rom(args.rom, args.vgm)
