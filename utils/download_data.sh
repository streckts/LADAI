#!/bin/bash

# Ensure data directory exists and switch to it
mkdir -p data
cd data

echo "Downloading structured HDFS CSV (100k labeled logs)..."
wget -nc https://raw.githubusercontent.com/logpai/loglizer/master/data/HDFS/HDFS_100k.log_structured.csv

echo "Downloading full raw HDFS logs archive (~162 MB)..."
wget -nc https://zenodo.org/record/3227177/files/HDFS_1.tar.gz

echo "Extracting HDFS_1.tar.gz..."
tar -xzf HDFS_1.tar.gz

echo "Rename extracted logs to HDFS.log for consistency..."
# The archive may contain files like HDFS.log, rename/move accordingly
# Adjust based on actual extracted filenames
mv HDFS.log ./HDFS.log || true

echo "Download and extraction complete. Files are in: $(pwd)"


