#!/usr/bin/python3
"""
log parsing in python
"""

import sys
import re

def output(log: dict) -> None:
    """
    displays stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))

if __name__ == "__main__":
    regex = re.compile(r'(\d{3}) (\d+)')

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {
            str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]
        }
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.match(line)
            if match:
                line_count += 1
                code, file_size = match.groups()
                file_size = int(file_size)

                # File size
                log["file_size"] += file_size

                # status code
                if code.isdigit():
                    log["code_frequency"][code] += 1

                if line_count % 10 == 0:
                    output(log)
    finally:
        output(log)

