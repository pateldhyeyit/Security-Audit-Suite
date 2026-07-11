# main.py

from rich.console import Console
from rich.panel import Panel

from database import Database

console = Console()


from modules.system_info import display_system_info
from modules.process_info import display_processes
from modules.network_info import display_network_info
from modules.file_integrity import monitor_file
from modules.reports import report_menu

from database import Database
from modules.logger import log_info

db = Database()

log_info("Application started.")
db.add_log("Application Started")


def system_information():
    display_system_info()

def process_information():
    display_processes()

def network_information():
    display_network_info()

def file_integrity():
    monitor_file()


def reports():
    report_menu()


def view_logs(db):
    logs = db.get_logs()

    if not logs:
        console.print("[red]No logs found.[/red]")
        return

    console.print("\n[bold cyan]Audit Logs[/bold cyan]\n")

    for log in logs:
        console.print(
            f"[green]{log[0]}[/green] | "
            f"{log[3]} | "
            f"{log[1]} | "
            f"{log[2]}"
        )


def menu():
    console.print(
        Panel.fit(
            "[bold cyan]Security Audit Suite[/bold cyan]\nVersion 1.0",
            title="Main Menu"
        )
    )

    print("1. System Information")
    print("2. Running Processes")
    print("3. Network Information")
    print("4. File Integrity Monitor")
    print("5. Reports")
    print("6. View Audit Logs")
    print("7. Exit")


def main():
    db = Database()

    db.add_log("Application Started")

    while True:

        menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            system_information()

        elif choice == "2":
            process_information()

        elif choice == "3":
            network_information()

        elif choice == "4":
            file_integrity()

        elif choice == "5":
            reports()

        elif choice == "6":
            view_logs(db)

        elif choice == "7":
            db.add_log("Application Closed")
            db.close()
            console.print("\nGoodbye!\n")
            break

        else:
            console.print("[red]Invalid choice.[/red]")

        input("\nPress Enter to continue...")
        console.clear()


if __name__ == "__main__":
    main()