# Log Anomaly Detection with AI

This project implements an end-to-end anomaly detection system for system logs using self-supervised machine learning. It focuses on modeling normal system behavior by learning patterns in real-world log data and detecting deviations that may indicate failures or suspicious activity. The project is designed to reflect practical IT and security use cases.

## Project Scope (Current)

Parses raw HDFS log files using the Drain3 log template mining algorithm

Extracts structured log templates and assigns cluster IDs (log keys)

Sessionizes logs by block ID to form sequences of system events

Prepares data for training a self-supervised LSTM model to predict normal log sequences

Evaluation is planned using the labeled HDFS_100k.log_structured.csv dataset

The LSTM will be trained on normal data only and evaluated on mixed normal/anomalous data to detect deviations from expected system behavior.

## Use Cases

Anomaly detection in distributed systems (e.g., Hadoop/HDFS)

Infrastructure and system log monitoring

Security and SOC analyst tooling foundations

Real-world simulation of IT log handling pipelines

## Tech Stack

Python

Drain3 (log parsing)

Pandas / NumPy

Regex (for block ID/session extraction)

PyTorch or TensorFlow (planned, for LSTM modeling)

Jupyter Notebooks (for data exploration/model training)

## File Structure

perl
Copy
Edit
log-anomaly-detector/
├── data/                  # (gitignored) Raw and structured HDFS logs  
├── parsed_logs/           # Parsed and sessionized output  
├── scripts/
│   └── download_data.sh   # Downloads raw + structured logs from Loghub  
├── utils/
│   ├── parse_logs.py      # Parses raw logs using Drain3  
│   └── sessionize_logs.py # Extracts sessions and sequences  
└── README.md
## Dataset

We use the publicly available HDFS log dataset from Loghub (https://github.com/logpai/loghub), which includes:

HDFS.log: raw, unstructured log lines

HDFS_100k.log_structured.csv: pre-parsed logs with anomaly labels for evaluation

To download the dataset, run:

bash
Copy
Edit
bash scripts/download_data.sh
## Future Plans

Train an LSTM model on sessionized sequences to predict the next log template

Flag events as anomalous if the predicted log deviates from expected patterns

Evaluate using true anomaly labels in the structured CSV

Optionally build a Streamlit interface for real-time sequence analysis