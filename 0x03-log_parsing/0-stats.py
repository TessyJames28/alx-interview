#!/usr/bin/python3
"""log parsing"""
import sys
import re


if __name__ == '__main__':
    """Log parsing function"""
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s{1}-\s\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{6}\]\s"GET\s\/projects\/260\sHTTP\/1.1"\s(\d{3})\s(\d+)$'  # nopep8

    codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0,
             '405': 0,  '500': 0}
    size = 0
    counter = 0

    try:
        for line in sys.stdin:
            counter += 1
            pattern = re.compile(pattern)
            match = re.match(pattern, str(line.strip()))
            if match:
                if int(match.group(1)):
                    codes[str(match.group(1))] += 1
                    size += int(match.group(2))

                    if counter == 10:
                        counter = 0
                        print("File size: {}".format(size))
                        for key, val in sorted(codes.items(),
                                               key=lambda x: x[0]):
                            if val != 0:
                                print("{}: {}".format(key, val))

    finally:
        print("File size: {}".format(size))
        for key, val in sorted(codes.items(), key=lambda x: x[0]):
            if val != 0:
                print("{}: {}".format(key, val))
