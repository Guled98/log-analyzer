# Log Analyzer

Simple Python log analyzer for detecting suspicious login attempts in server logs.

## Overview

This project demonstrates a basic security analysis technique where log files are analyzed to detect suspicious activity such as repeated failed login attempts from the same IP address.

The script scans a log file and identifies IP addresses with multiple failed login attempts.

## Features

- Detects failed login attempts
- Counts suspicious IP activity
- Alerts when brute-force behaviour is detected
- Shows top attacker IP

## Technologies

- Python
- Log analysis
- Basic SOC detection concepts
  
## Files

`log_analyzer.py`  
Python script that analyzes log files.

`sample_log.txt`  
Example log file for testing.

## How to run

Download or clone the repository, then run:

```bash
python log_analyzer.py
```

## Example Output

```text
=== Suspicious Activity Report ===

192.168.1.10 -> 3 failed login attempts
ALERT: Possible brute-force attack from 192.168.1.10

192.168.1.22 -> 1 failed login attempts

Top attacker IP: 192.168.1.10 (3 failed attempts)
```

## Author

Guled Abdulgadir Mohamed  
Cybersecurity Student – Kristiania University College
