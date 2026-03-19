import json
from collections import defaultdict

log_file = "conn.log"
scan_tracker = defaultdict(lambda: defaultdict(set))
alerts = []

with open(log_file, "r") as f:
	for line in f:
		line = line.strip()

		if not line:
			continue

		try:
			data = json.loads(line)
		except:
			continue

		src_ip = data.get("id.orig_h")
		dst_port = data.get("id.resp_p")
		dst_ip = data.get("id.resp_h")

		#Ignore internal admin network noise
		if src_ip and src_ip.startswith("192.168.10."):
			continue

		if src_ip and dst_port:
			scan_tracker[src_ip][dst_ip].add(str(dst_port))


THRESHOLD = 100

print("\n--- Autonomous Port Scan Detection Report ---\n")
print(f"DEBUG: total source IPs seen = {len(scan_tracker)}")

alerts_found =  False

for src_ip, targets in scan_tracker.items():
	for dst_ip, ports in targets.items():
		if len(ports) < 5:
			continue

		print(f"DEBUG -> {src_ip} -> {dst_ip}: {len(ports)} unique ports")

		if len(ports) > THRESHOLD:
			alerts_found = True

		alert = {

			"type": "port scan",
			"attacker": src_ip,
			"target": dst_ip,
			"port_count": len(ports),
			"sample_ports": sorted(list(ports), key=int)[:15],
			"severity": "high"
		}

		alerts.append(alert)

		print("\n[ALERT] Port Scan Detected")
		print(json.dumps(alert, indent =2))
if alerts:
	with open("aletrs.json", "w") as f:
		json.dump(alerts, f, indent=2)
	print("\n[+] Alerts saved to alerts.json\n")
else:
	print("\n[+] No alerts to save.\n")
