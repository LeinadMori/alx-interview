#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    global total_size, status_code_counts
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            ip, dash, date, method, url, protocol, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]
            if method != '"GET' or url != '/projects/260' or protocol != 'HTTP/1.1"':
                continue
            
            status_code = int(status_code)
            file_size = int(file_size)

            total_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_statistics()

        except (ValueError, IndexError):
            continue

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

# Print final statistics if the script ends naturally
print_statistics()
