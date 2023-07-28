#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """return true or false if utf-8 validated"""
    byte = 0

    for bits in data:
        if byte == 0:
            if bits >> 5 == 0b110 or bits >> 5 == 0b1110:
                byte += 1
            elif bits >> 4 == 0b1110:
                byte += 2
            elif bits >> 3 == 0b11110:
                byte += 3
            elif bits >> 7 == 0b1:
                return False
        else:
            if bits >> 6 != 0b10:
                return False
            byte -= 1
    return byte == 0
