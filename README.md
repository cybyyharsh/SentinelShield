# SentinelShield  
## Advanced Intrusion Detection & Web Protection System

SentinelShield is a hands-on cybersecurity project that simulates the core behavior
of a lightweight Web Application Firewall (WAF).  
The system inspects HTTP requests, detects malicious patterns, monitors abusive
traffic behavior, and generates security logs for analysis.

---

## 🔍 Features
- HTTP request inspection
- Signature-based attack detection:
  - SQL Injection
  - Cross-Site Scripting (XSS)
  - Directory Traversal
- Behavior-based detection using rate limiting
- Real-time request blocking
- Security logging with SOC-style analysis
- Log analysis and attack summary reporting

---

## 🛠️ Technologies Used
- Kali Linux
- Python 3
- Flask
- curl (for attack simulation)

---

## ⚙️ How It Works
1. Incoming HTTP requests are inspected.
2. Requests are matched against predefined attack signatures.
3. Request frequency is monitored to detect abuse.
4. Malicious or abusive requests are blocked.
5. Security events are logged.
6. Logs are analyzed to generate attack summaries.

---

## 🚀 How to Run (Kali Linux)

```bash
git clone https://github.com/yourusername/SentinelShield.git
cd SentinelShield
pip install flask
python3 sentinelshield.py
