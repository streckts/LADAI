import re
import pandas as pd

def parse_log(file_path):
    pattern = re.compile(r"(?P<timestamp>[\w\s:]+) .* (?P<service>\w+)\[\d+\]: (?P<message>.+)")
    logs = []
    with open(file_path, 'r') as f:
        for line in f:
            match = pattern.match(line)
            if match:
                logs.append(match.groupdict())
    return pd.DataFrame(logs)
