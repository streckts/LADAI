from drain3 import TemplateMiner
from drain3.file_persistence import FilePersistence
import pandas as pd
import re
import os

def parse_hdfs_logs(input_path, output_path):
    # Use persistent template state so reruns keep learned structure
    persistence = FilePersistence("drain3_state.json")
    template_miner = TemplateMiner()

    logs = []
    with open(input_path, "r") as file:
        for line in file:
            match = re.search(r":\s(.+)", line)
            if not match:
                continue
            message = match.group(1)

            # Feed to Drain3
            result = template_miner.add_log_message(message)
            if result is None:
                continue

            logs.append({
                "raw_log": line.strip(),
                "parsed_message": message,
                "log_template": result["template_mined"],
                "cluster_id": result["cluster_id"]
            })

    # Save to CSV
    df = pd.DataFrame(logs)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} parsed logs to {output_path}")

# DEFAULT
if __name__ == "__main__":
    input_file = "data/HDFS_2k.log"
    output_file = "parsed_logs/hdfs_parsed.csv"
    parse_hdfs_logs(input_file, output_file)
