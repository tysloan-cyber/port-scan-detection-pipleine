# Autonomous Port Scan Detection Pipeline

## Overview
This project simulates a real-world cybersecurity detection pipeline using a segmented virtual network. It ingests network telemetry from Zeek (Security Onion), analyzes connection behavior, and identifies port scanning activity using Python-based detection logic.

## Objective
To build a hands-on system that:
- Processes real network logs
- Detects suspicious behavior (port scans)
- Correlates attacker and target activity
- Outputs structured alerts for further automation

---

## Architecture

### Network Segmentation
- LAN: 192.168.10.0/24
- DMZ: 192.168.20.0/24
- ATTACK: 192.168.30.0/24

### Components
- pfSense: Firewall and routing
- Security Onion: Log collection (Zeek)
- Kali Linux: Attack simulation
- Metasploitable / Web Server: Targets
- Admin Box: Log processing and detection

---

## Workflow

1. Generate traffic (Nmap scans from Kali)
2. Capture logs via Zeek (Security Onion)
3. Transfer logs via SCP
4. Parse logs using Python
5. Detect port scanning behavior
6. Output alerts to terminal and JSON file

---

## Detection Logic

The system tracks:
