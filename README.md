# Security Audit Suite

**Security Audit Suite** is a lightweight Python CLI tool that collects basic system/network/process information, monitors a file’s integrity (SHA-256 baseline), stores audit events in a local SQLite database, and can export logs to JSON/CSV.

> This project is intended for educational and local auditing purposes.

## Features

- **System Information**: hostname, OS details, CPU/RAM/Disk usage, boot time
- **Running Processes**: top processes by CPU usage
- **Network Information**: interface details + basic network I/O statistics
- **File Integrity Monitor**: detects changes to a single file using stored SHA-256 hashes
- **Audit Logs**: records app events in `data/security_audit.db`
- **Reports**: export audit logs to:
  - `reports/report.json`
  - `reports/report.csv`

## Project Structure

- `main.py` - CLI menu entrypoint
- `config.py` - paths and constants (data/log/report directories)
- `database.py` - SQLite DB wrapper
- `modules/` - feature modules (system/process/network/file integrity/reports/logger)
- `data/` - SQLite database + stored file hashes
- `logs/` - `audit.log`
- `reports/` - exported reports

## Requirements

- Python 3.8+ recommended

Install dependencies:

```bash
pip install -r requirements.txt
```

Dependencies include: `psutil`, `rich`, `requests`, `netifaces`, `python-dateutil`, etc. (see `requirements.txt`).

## Setup & Run

### 1) (Recommended) Create a virtual environment

```bash
python -m venv .venv
.[0mvenv\Scripts\activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Start the application

```bash
python main.py
```

## How to Use

After launching, you’ll see a menu:

1. **System Information**
   - Displays local OS + resource information.

2. **Running Processes**
   - Shows the top running processes (default limit is 25).

3. **Network Information**
   - Prints network interface details and local network I/O statistics.

4. **File Integrity Monitor**
   - Prompts: `Enter file path:`
   - If the file has no baseline hash yet, it creates one in `data/hashes.json`.
   - If a baseline exists and the hash differs, it shows old/new hashes and lets you update the stored baseline.

5. **Reports**
   - Export audit logs to JSON or CSV.

6. **View Audit Logs**
   - Displays recent audit log entries stored in SQLite.

7. **Exit**
   - Closes the database and exits.

## Data & Output Locations

- SQLite DB: `data/security_audit.db`
- File hash baselines: `data/hashes.json`
- Log file: `logs/audit.log`
- JSON report: `reports/report.json`
- CSV report: `reports/report.csv`

## Notes / Limitations

- File integrity monitoring is **per-file** and based on **SHA-256**; it’s not a full file tree integrity scanner.
- The app collects **local** information only.

## License

MIT

