import pandas as pd
import re
import os

def extract_block_id(log_line):
    """Extracts HDFS block ID (e.g., blk_123456) from the raw log line."""
    match = re.search(r'(blk_\d+)', log_line)
    return match.group(1) if match else None

def sessionize(parsed_csv_path, output_path):
    df = pd.read_csv(parsed_csv_path)

    # Extract session ID (block ID) from each raw log line
    df["block_id"] = df["raw_log"].apply(extract_block_id)

    # Drop any rows where block_id could not be extracted
    df = df.dropna(subset=["block_id"])

    # Group by block ID and collect sequences of cluster IDs
    sessions = df.groupby("block_id")["cluster_id"].apply(list).reset_index()

    # Save as CSV with 2 columns: block_id, cluster_sequence
    sessions.rename(columns={"cluster_id": "cluster_sequence"}, inplace=True)
    sessions.to_csv(output_path, index=False)
    print(f"Saved {len(sessions)} sessions to {output_path}")

if __name__ == "__main__":
    input_csv = "parsed_logs/hdfs_parsed.csv"
    output_csv = "parsed_logs/hdfs_sessions.csv"
    sessionize(input_csv, output_csv)
