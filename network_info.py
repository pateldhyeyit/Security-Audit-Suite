# modules/network_info.py

import psutil
import socket
from rich.console import Console
from rich.table import Table

console = Console()


def format_bytes(num):
    """Convert bytes to KB, MB, GB..."""

    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if num < 1024:
            return f"{num:.2f} {unit}"
        num /= 1024

    return f"{num:.2f} PB"


def display_network_info():
    """Display local network information."""

    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except Exception:
        ip_address = "Unknown"

    console.print(f"\nHostname : [cyan]{hostname}[/cyan]")
    console.print(f"IP Address : [green]{ip_address}[/green]\n")

    table = Table(title="Network Interfaces")

    table.add_column("Interface", style="cyan")
    table.add_column("IPv4 Address")
    table.add_column("Netmask")
    table.add_column("MAC Address")

    interfaces = psutil.net_if_addrs()

    for interface_name, addresses in interfaces.items():

        ipv4 = ""
        netmask = ""
        mac = ""

        for address in addresses:

            if address.family == socket.AF_INET:
                ipv4 = address.address
                netmask = address.netmask

            elif str(address.family) == "AddressFamily.AF_LINK":
                mac = address.address

        table.add_row(
            interface_name,
            ipv4,
            netmask,
            mac
        )

    console.print(table)

    stats = psutil.net_io_counters()

    console.print("\n[bold cyan]Network Statistics[/bold cyan]\n")

    console.print(
        f"Bytes Sent     : {format_bytes(stats.bytes_sent)}"
    )

    console.print(
        f"Bytes Received : {format_bytes(stats.bytes_recv)}"
    )

    console.print(
        f"Packets Sent   : {stats.packets_sent}"
    )

    console.print(
        f"Packets Received : {stats.packets_recv}"
    )


if __name__ == "__main__":
    display_network_info()