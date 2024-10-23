#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_codes = set(status_codes.keys())
line_count = 0

def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def handle_sigint(signum, frame):
    """Handles the keyboard interrupt (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Attach signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_sigint)

# Read input line by line from stdin
try:
    for line in sys.stdin:
        line_count += 1

        # Split the line into parts
        parts = line.split()
        if len(parts) < 7:
            continue

        # Extract the status code and file size
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        # Accumulate file size and status code counts
        total_file_size += file_size
        if status_code in valid_codes:
            status_codes[status_code] += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
