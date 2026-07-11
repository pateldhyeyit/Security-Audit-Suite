# modules/file_integrity.py

import hashlib
import json
from pathlib import Path

from config import HASH_FILE


def calculate_sha256(file_path):
    """
    Calculate SHA-256 hash of a file.
    """

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)

            if not chunk:
                break

            sha256.update(chunk)

    return sha256.hexdigest()


def load_hashes():
    """
    Load stored hashes from JSON file.
    """

    if not HASH_FILE.exists():
        return {}

    with open(HASH_FILE, "r") as file:
        return json.load(file)


def save_hashes(hashes):
    """
    Save hashes to JSON.
    """

    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)


def monitor_file():
    """
    Monitor a single file for changes.
    """

    path = input("Enter file path: ").strip()

    file_path = Path(path)

    if not file_path.exists():
        print("\nFile not found.")
        return

    hashes = load_hashes()

    current_hash = calculate_sha256(file_path)

    key = str(file_path.resolve())

    if key not in hashes:

        hashes[key] = current_hash
        save_hashes(hashes)

        print("\nBaseline hash created.")
        print("Run again later to detect changes.")

        return

    if hashes[key] == current_hash:

        print("\nNo changes detected.")

    else:

        print("\nWARNING: File has changed!")

        print("\nOld Hash")
        print(hashes[key])

        print("\nNew Hash")
        print(current_hash)

        choice = input("\nUpdate stored hash? (y/n): ").lower()

        if choice == "y":
            hashes[key] = current_hash
            save_hashes(hashes)
            print("Hash updated.")


if __name__ == "__main__":
    monitor_file()