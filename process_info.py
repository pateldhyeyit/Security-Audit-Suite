# modules/process_info.py

import psutil
from rich.console import Console
from rich.table import Table

console = Console()


def get_processes():
    """
    Get information about running processes.
    """

    processes = []

    for process in psutil.process_iter(
        ['pid', 'name', 'cpu_percent', 'memory_percent', 'status']
    ):

        try:
            processes.append({
                "pid": process.info["pid"],
                "name": process.info["name"],
                "cpu": process.info["cpu_percent"],
                "memory": round(process.info["memory_percent"], 2),
                "status": process.info["status"]
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    return sorted(
        processes,
        key=lambda p: p["cpu"],
        reverse=True
    )


def display_processes(limit=25):
    """
    Display top running processes.
    """

    processes = get_processes()

    table = Table(title="Running Processes")

    table.add_column("PID", justify="right", style="cyan")
    table.add_column("Process Name", style="green")
    table.add_column("CPU %", justify="right")
    table.add_column("Memory %", justify="right")
    table.add_column("Status")

    for process in processes[:limit]:

        table.add_row(
            str(process["pid"]),
            str(process["name"]),
            f'{process["cpu"]:.1f}',
            f'{process["memory"]:.2f}',
            process["status"]
        )

    console.print(table)


if __name__ == "__main__":
    display_processes()