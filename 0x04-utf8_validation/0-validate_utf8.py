#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """return true or false if utf-8 validated"""
    x = "01111111"
    if not data:
        return False
    for i in data:
        if bin(i)[2:].zfill(8) > x:
            return False
        return True
