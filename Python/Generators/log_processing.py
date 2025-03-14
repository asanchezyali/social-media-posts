# Processing a large log file efficiently
def parse_log_line(line):
    # Extract timestamp and message
    parts = line.split(" ", 1)
    return {"timestamp": parts[0], "message": parts[1]}

def filter_errors(log_entries):
    for entry in log_entries:
        if "ERROR" in entry["message"]:
            yield entry

def process_logs(filename):
    with open(filename) as f:
        # Parse each line
        entries = (parse_log_line(line) for line in f)
        # Filter for errors
        errors = filter_errors(entries)
        # Group by hour
        for error in errors:
            yield error