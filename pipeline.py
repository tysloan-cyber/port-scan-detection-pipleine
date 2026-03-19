import os

SECURITY_ONION_IP = "192.168.10.20"
REMOTE_LOG = "/nsm/zeek/logs/current/conn.log"
LOCAL_LOG = "conn.log"

print("\n[+] Pulling logs from Security Onion...")
os.system(f"scp adminty@{SECURITY_ONION_IP}:{REMOTE_LOG} {LOCAL_LOG}")

print("[+] Running detection script...\n")
os.system("python3 port_scan_detector.py")
