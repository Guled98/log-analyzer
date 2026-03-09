# Log Analyzer

Simple Python log analyzer for detecting suspicious login attempts in server logs.

## Overview

This project demonstrates a basic security analysis technique where log files are analyzed to detect suspicious activity such as repeated failed login attempts from the same IP address.

The script scans a log file and identifies IP addresses with multiple failed login attempts.

## Technologies

- Python
- Log analysis
- Basic security monitoring concepts

## Files

log_analyzer.py  
Python script that analyzes log files for suspicious activity.

sample_log.txt  
Example log file used to test the analyzer.

## Example Output
Suspicious activity detected:

192.168.1.10 -> 3 failed login attempts
192.168.1.22 -> 1 failed login attempts

## Why this project

Understanding how to analyze logs is an important part of cybersecurity and SOC (Security Operations Center) work.  
This project demonstrates a simple approach to detecting suspicious authentication activity.

## Author

Guled Abdulgadir Mohamed  
Cybersecurity Student – Kristiania University College
