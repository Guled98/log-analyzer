# Simple Log Analyzer

log_file = "sample_log.txt"

suspicious_ips = {}

with open(log_file, "r") as file:
    for line in file:
        if "FAILED LOGIN" in line:
            ip = line.split()[-1]
            if ip in suspicious_ips:
                suspicious_ips[ip] += 1
            else:
                suspicious_ips[ip] = 1

print("Suspicious activity detected:\n")

for ip, attempts in suspicious_ips.items():
    print(f"{ip} -> {attempts} failed login attempts")
