#!/bin/bash

# Create data directory if it doesn't exist
mkdir -p data
cd data

echo "Downloading HDFS dataset from Loghub..."

# Download structured CSV (with anomaly labels)
wget -nc https://zenodo.org/record/3227177/files/HDFS_100k.log_structured.csv

# Download raw HDFS.log file
wget -nc https://zenodo.org/record/3227177/files/HDFS.log

echo "Download complete. Files saved in ./data/"