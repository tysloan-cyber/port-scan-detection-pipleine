# Port Scan Detection Pipeline

## Overview
This project demonstrates a cybersecurity detection pipeline built in a virtualized homelab environment. It processes Zeek (Security Onion) network logs and identifies port scanning activity using Python-based behavioral analysis.

---

## Objective
Build a system that can:
- Ingest real network telemetry
- Detect port scanning behavior
- Correlate attacker and target activity
- Generate structured alerts for further analysis

---

## Architecture

### Network Segmentation
- **LAN:** 192.168.10.0/24  
- **DMZ:** 192.168.20.0/24  
- **ATTACK:** 192.168.30.0/24  

### Components
- **pfSense** – Routing and segmentation  
- **Security Onion (Zeek)** – Log collection  
- **Kali Linux** – Attack simulation  
- **DMZ Hosts** – Targets (Web Server / Metasploitable)  
- **Admin Box** – Log processing and detection  

---

## Technologies
- Python
- VirtualBox
- pfSense
- Security Onion (Zeek)
- Linux (Ubuntu, Kali)

---

## Project Structure
- pipeline.py # Automates log retrieval and execution
- port_scan_detector.py # Core detection logic
- alerts.json # Sample detection output
- study_notes.txt # Interview preparation notes

---

## Workflow

1. Generate traffic from attacker (Kali Linux)
2. Capture logs using Zeek (Security Onion)
3. Transfer logs via SCP
4. Parse logs using Python
5. Detect port scanning behavior
6. Output alerts (terminal + JSON)

---

## Detection Logic

The system tracks:

If a source connects to a large number of unique ports on a target, it is flagged as a potential port scan.

---

## Future Enhancements
- Cloud deployment (AWS S3 + Lambda)
- Real-time log processing
- Docker containerization
- AI-assisted alert analysis
---

## 🚨 Example Alert

```json
{
  "type": "port_scan",
  "attacker": "192.168.30.100",
  "target": "192.168.20.20",
  "port_count": 65535,
  "severity": "high"
}

