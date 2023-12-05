import sys
import signal

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

def print_statistics():
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) == 7:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
