# modules/reports.py

import csv
import json

from config import DEFAULT_CSV_REPORT, DEFAULT_JSON_REPORT
from database import Database


def export_json():
    """
    Export audit logs to JSON.
    """

    db = Database()

    logs = db.get_logs(limit=100000)

    report = []

    for log in logs:

        report.append(
            {
                "id": log[0],
                "action": log[1],
                "details": log[2],
                "timestamp": log[3]
            }
        )

    with open(DEFAULT_JSON_REPORT, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    db.close()

    print(f"\nJSON report saved to:\n{DEFAULT_JSON_REPORT}")


def export_csv():
    """
    Export audit logs to CSV.
    """

    db = Database()

    logs = db.get_logs(limit=100000)

    with open(DEFAULT_CSV_REPORT, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Action",
            "Details",
            "Timestamp"
        ])

        for log in logs:

            writer.writerow(log)

    db.close()

    print(f"\nCSV report saved to:\n{DEFAULT_CSV_REPORT}")


def report_menu():

    while True:

        print("\n========== Reports ==========")

        print("1. Export JSON")
        print("2. Export CSV")
        print("3. Back")

        choice = input("\nSelect Option: ")

        if choice == "1":
            export_json()

        elif choice == "2":
            export_csv()

        elif choice == "3":
            break

        else:
            print("\nInvalid Option")


if __name__ == "__main__":
    report_menu()