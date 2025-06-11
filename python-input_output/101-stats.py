#!/usr/bin/python3

"""Reads from standard input and computes metrics.

After every ten lines or a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): Total read file size.
        status_codes (dict): Count of each status code.
    """
    print("File size: {}".format(size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    import sys

    size = 0
    count = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            count += 1
            parts = line.strip().split()

            # Safely parse file size
            try:
                size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            # Safely parse status code
            try:
                code = parts[-2]
                if code in valid_codes:
                    status_codes[code] = status_codes.get(code, 0) + 1
            except IndexError:
                pass

            # Print stats every 10 lines
            if count % 10 == 0:
                print_stats(size, status_codes)

        # Final stats (for remaining lines < 10 or end of file)
        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
