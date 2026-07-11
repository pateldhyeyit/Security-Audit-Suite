# config.py

from pathlib import Path

# -----------------------------
# Project Information
# -----------------------------
APP_NAME = "Security Audit Suite"
VERSION = "1.0.0"

# -----------------------------
# Directories
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
REPORT_DIR = BASE_DIR / "reports"

# Create directories if they don't exist
for directory in (DATA_DIR, LOG_DIR, REPORT_DIR):
    directory.mkdir(exist_ok=True)

# -----------------------------
# Database
# -----------------------------
DATABASE_PATH = DATA_DIR / "security_audit.db"

# -----------------------------
# Logging
# -----------------------------
LOG_FILE = LOG_DIR / "audit.log"

# -----------------------------
# File Integrity Monitoring
# -----------------------------
HASH_FILE = DATA_DIR / "hashes.json"

# -----------------------------
# Report Export
# -----------------------------
DEFAULT_JSON_REPORT = REPORT_DIR / "report.json"
DEFAULT_CSV_REPORT = REPORT_DIR / "report.csv"

# -----------------------------
# Port Scanner
# -----------------------------
DEFAULT_TIMEOUT = 1.0
MAX_PORT = 1024

# -----------------------------
# CLI
# -----------------------------
MENU_TITLE = "Security Audit Suite"

# -----------------------------
# Colors (Rich)
# -----------------------------
PRIMARY_COLOR = "cyan"
SUCCESS_COLOR = "green"
WARNING_COLOR = "yellow"
ERROR_COLOR = "red"