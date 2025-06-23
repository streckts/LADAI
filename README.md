# Log Anomaly Detection with AI

This project implements a lightweight anomaly detection system for system logs using machine learning. It demonstrates how AI can enhance traditional IT monitoring by automatically identifying suspicious or irregular log events—useful for early warning systems, intrusion detection, and infrastructure monitoring.

## Overview

- Parses and processes system log files (e.g., Linux `auth.log`, HDFS logs)
- Extracts features using TF-IDF or custom encoding
- Applies machine learning models (e.g., Isolation Forest) for anomaly detection
- Displays results via a simple Streamlit-based web interface

## Use Cases

- IT security monitoring
- Log event summarization and filtering
- SOC analyst tooling enhancement
- AI-based alert triaging

## Tech Stack

- Python
- Scikit-learn (placeholder)
- Pandas / NumPy
- Streamlit (UI potentially)
- Regex-based log parsing
