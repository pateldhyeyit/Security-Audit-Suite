# database.py

import sqlite3
from datetime import datetime
from config import DATABASE_PATH


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Create required database tables."""

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT NOT NULL,
            details TEXT,
            created_at TEXT NOT NULL
        )
        """)

        self.conn.commit()

    def add_log(self, action, details=""):
        """Insert an audit log."""

        self.cursor.execute(
            """
            INSERT INTO audit_logs(action, details, created_at)
            VALUES (?, ?, ?)
            """,
            (
                action,
                details,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        )

        self.conn.commit()

    def get_logs(self, limit=100):
        """Return latest audit logs."""

        self.cursor.execute(
            """
            SELECT id, action, details, created_at
            FROM audit_logs
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        return self.cursor.fetchall()

    def clear_logs(self):
        """Delete all audit logs."""

        self.cursor.execute("DELETE FROM audit_logs")
        self.conn.commit()

    def close(self):
        self.conn.close()


# -------------------------
# Simple Test
# -------------------------

if __name__ == "__main__":

    db = Database()

    db.add_log(
        "Program Started",
        "Security Audit Suite launched."
    )

    print("\nLatest Logs\n")

    for log in db.get_logs():

        print(
            f"[{log[0]}] "
            f"{log[3]} | "
            f"{log[1]} | "
            f"{log[2]}"
        )

    db.close()