import pandas as pd
import ast
import numpy as np
import os
import json

def generate_lstm_pairs(session_csv_path, output_dir, sequence_length=4):
    df = pd.read_csv(session_csv_path)

    X = []
    y = []

    for row in df.itertuples():
        try:
            sequence = ast.literal_eval(row.cluster_sequence)
        except (ValueError, SyntaxError):
            continue

        if len(sequence) <= sequence_length:
            continue

        for i in range(len(sequence) - sequence_length):
            input_seq = sequence[i:i+sequence_length]
            target = sequence[i+sequence_length]
            X.append(input_seq)
            y.append(target)

    X = np.array(X, dtype=np.int32)
    y = np.array(y, dtype=np.int32)

    os.makedirs(output_dir, exist_ok=True)
    np.save(os.path.join(output_dir, "X.npy"), X)
    np.save(os.path.join(output_dir, "y.npy"), y)

    # Save cluster_id metadata (e.g., for embedding size)
    unique_ids = sorted(set(np.concatenate([X.flatten(), y])))
    meta = {
        "num_unique_cluster_ids": len(unique_ids),
        "unique_cluster_ids": unique_ids,
        "sequence_length": sequence_length
    }
    with open(os.path.join(output_dir, "meta.json"), "w") as f:
        json.dump(meta, f, indent=2)

    print(f"Saved {len(X)} input/output pairs to {output_dir}")

if __name__ == "__main__":
    input_path = "parsed_logs/hdfs_sessions.csv"
    output_path = "model_data/"
    generate_lstm_pairs(input_path, output_path, sequence_length=4)
