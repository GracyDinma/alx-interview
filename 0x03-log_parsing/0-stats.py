#!/usr/bin/python3
"""
Log parsing
"""

import sys
import re

def print_stats(stats: dict, file_size: int) -> None:
    """Print the accumulated statistics."""
    print("File size: {}".format(file_size))
    for code in sorted(stats):
        if stats[code] > 0:
            print("{}: {}".format(code, stats[code]))

if __name__ == '__main__':
    # Regular expression for parsing the log lines
    regex = re.compile(
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )

    line_count = 0
    file_size = 0
    stats = {code: 0 for code in ["200", "301", "400", "401", "403", "404", "405", "500"]}

    try:
        for line in sys.stdin:
            line_count += 1
            match = regex.fullmatch(line.strip())
            if match:
                status_code = match.group(3)
                file_size += int(match.group(4))
                if status_code in stats:
                    stats[status_code] += 1

            # Output statistics every 10 lines
            if line_count % 10 == 0:
                print_stats(stats, file_size)

        # Print final statistics
        print_stats(stats, file_size)

    except KeyboardInterrupt:
        # Print statistics on user interrupt
        print_stats(stats, file_size)
        sys.exit(0)
    except Exception as e:
        print(f"Error processing line: {e}")
