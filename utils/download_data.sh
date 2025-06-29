#!/bin/bash

mkdir -p data
cd data

echo "Downloading structured CSV..."
wget -nc https://raw.githubusercontent.com/logpai/loglizer/master/data/HDFS/HDFS_100k.log_structured.csv

echo "Downloading small HDFS sample (2k lines)..."
wget -nc https://raw.githubusercontent.com/logpai/loghub/master/HDFS/HDFS_2k.log

echo "Done. CSV and sample log are in ./data/"
