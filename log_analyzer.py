# Simple Log Analyzer with basic brute-force detection

log_file = "sample_log.txt"
suspicious_ips = {}

with open(log_file, "r") as file:
    for line in file:
        if "FAILED LOGIN" in line:
            ip = line.split()[-1]
            suspicious_ips[ip] = suspicious_ips.get(ip, 0) + 1

print("=== Suspicious Activity Report ===\n")

if not suspicious_ips:
    print("No suspicious activity detected.")
else:
    top_ip = max(suspicious_ips, key=suspicious_ips.get)

    for ip, attempts in suspicious_ips.items():
        print(f"{ip} -> {attempts} failed login attempts")

        if attempts >= 3:
            print(f"ALERT: Possible brute-force attack from {ip}\n")

    print(f"Top attacker IP: {top_ip} ({suspicious_ips[top_ip]} failed attempts)")
