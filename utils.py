# modules/utils.py

import os
import platform
from datetime import datetime

from rich.console import Console

console = Console()

def clear_screen():
    console.clear()


def clear_screen():
    """
    Clear terminal screen.
    """

    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def pause():
    """
    Pause execution.
    """

    input("\nPress Enter to continue...")


def print_header(title):
    """
    Print application header.
    """

    print("=" * 60)
    print(title.center(60))
    print("=" * 60)


def bytes_to_human(size):
    """
    Convert bytes into readable format.
    """

    units = ["B", "KB", "MB", "GB", "TB"]

    value = float(size)

    for unit in units:

        if value < 1024:
            return f"{value:.2f} {unit}"

        value /= 1024

    return f"{value:.2f} PB"


def current_time():
    """
    Return current date and time.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_choice(minimum, maximum):
    """
    Get validated integer input.
    """

    while True:

        try:

            choice = int(input("\nEnter Choice : "))

            if minimum <= choice <= maximum:
                return choice

            print(f"Please enter a number between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def yes_no(question):
    """
    Ask yes/no question.
    """

    while True:

        answer = input(f"{question} (y/n): ").lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("Please enter y or n.")