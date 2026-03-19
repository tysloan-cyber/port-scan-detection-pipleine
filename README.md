# Port Scan Detection Pipeline

## Overview
This project is a homelab-based cybersecurity detection pipeline that identifies port scanning activity using Zeek logs collected by Security Onion and Python-based analysis.

## Goal
The goal of this project was to build a system that could:
- ingest real network telemetry
- detect suspicious port scanning behavior
- identify the attacker and target
- generate structured alert output

## Lab Environment
- pfSense (network segmentation)
- Security Onion (Zeek logs)
- Kali Linux (attacker)
- DMZ targets (Metasploitable / Web server)
- Admin Box (log analysis)

## Workflow
1. Generate traffic from attacker machine
2. Capture logs with Zeek
3. Transfer logs via SCP
4. Parse logs using Python
5. Detect port scanning behavior
6. Output alerts (terminal + JSON)

## Detection Logic
The system tracks:

source IP → destination IP → unique destination ports

If a source connects to many ports on a target, it is flagged as a port scan.

## Example Output
- Attacker: 192.168.30.100
- Target: 192.168.20.20
- Ports scanned: 65535

## Files
- `pipeline.py`
- `port_scan_detector.py`
- `alerts.json`

## Skills Demonstrated
- Python scripting
- log parsing
- behavior-based detection
- network analysis
- security automation

## Future Improvements
- AWS deployment
- real-time detection
- Docker containerization
- AI-based alert explanation
