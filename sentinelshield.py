from flask import Flask, request
import time
import re
from collections import defaultdict

app = Flask(__name__)

# Simple in-memory tracking
request_count = defaultdict(list)

# Log file
LOG_FILE = "logs/security.log"

# Attack signatures (basic simulation)
ATTACK_PATTERNS = {
    "SQL Injection": r"(\bor\b|\band\b).*?=|('|--|;)",
    "XSS": r"<script>|</script>",
    "Directory Traversal": r"\.\./",
    "Command Injection": r";|\|\|"
}

RATE_LIMIT = 10      # requests
TIME_WINDOW = 10     # seconds


def log_event(ip, attack_type, action):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"{timestamp} | {ip} | {attack_type} | {action}\n")


def is_rate_limited(ip):
    now = time.time()
    request_count[ip] = [t for t in request_count[ip] if now - t < TIME_WINDOW]
    request_count[ip].append(now)

    if len(request_count[ip]) > RATE_LIMIT:
        return True
    return False


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def inspect_request(path):
    ip = request.remote_addr
    payload = request.query_string.decode()

    # Rate limiting check
    if is_rate_limited(ip):
        log_event(ip, "Rate Limit Abuse", "Blocked")
        return "Request Blocked: Too many requests", 429

    # Signature detection
    for attack, pattern in ATTACK_PATTERNS.items():
        if re.search(pattern, payload, re.IGNORECASE):
            log_event(ip, attack, "Blocked")
            return f"Request Blocked: {attack} detected", 403

    log_event(ip, "Normal Request", "Allowed")
    return "Request Allowed", 200


if __name__ == "__main__":
    print("[+] SentinelShield running on http://127.0.0.1:5000")
    app.run(debug=False)
