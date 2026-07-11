import os
import platform
import socket
from datetime import datetime

import psutil
from rich.console import Console
from rich.table import Table

console = Console()


def bytes_to_gb(value):
    """Convert bytes to GB."""
    return round(value / (1024 ** 3), 2)


def get_system_info():
    """Collect local system information."""

    boot_time = datetime.fromtimestamp(psutil.boot_time())

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Username": os.getlogin(),
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": platform.python_version(),
        "CPU Cores": psutil.cpu_count(logical=True),
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "RAM Total (GB)": bytes_to_gb(memory.total),
        "RAM Used (%)": memory.percent,
        "Disk Total (GB)": bytes_to_gb(disk.total),
        "Disk Used (%)": disk.percent,
        "Boot Time": boot_time.strftime("%Y-%m-%d %H:%M:%S")
    }


def display_system_info():
    """Display collected information."""

    info = get_system_info()

    table = Table(title="System Information")

    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    for key, value in info.items():
        table.add_row(key, str(value))

    console.print(table)


if __name__ == "__main__":
    display_system_info()