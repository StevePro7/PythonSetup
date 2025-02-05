def process_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line          # Yield one line at a time


def analyze_log(line: str):
    print(line)
    pass


for log_line in process_log_file("server.log"):
    analyze_log(log_line)
