#!/usr/bin/env python3
"""generate_asset_structure.py

This script creates the recommended asset folder structure for a contributor.

Run this script once to set up your personal asset directories inside the
repository. You can pass your GitHub username as a command-line argument; if you
don't, the script will prompt you to enter a username and will continue prompting
until you provide one. It will then create the following structure:

assets/<username>/
    3d-assets/
        models/
        materials/
        scenes/
    2d-assets/
        sprites/
        ui/
        textures/
    audio/
        sound-effects/
        music/
    misc/

If the script is run in a non-interactive environment (e.g. by double-clicking without a terminal),
and cannot read input, it will print an error and exit gracefully. To avoid this, run the script
from a terminal or supply the username as a command-line argument.
"""

from pathlib import Path
import sys


REPO_ROOT = Path(__file__).resolve().parent.parent
ASSETS_ROOT = REPO_ROOT / "assets"


def create_structure(base_path: Path) -> Path:
    """Create the folder structure given a base path."""
    subfolders = [
        Path("3d-assets") / "models",
        Path("3d-assets") / "materials",
        Path("3d-assets") / "scenes",
        Path("2d-assets") / "sprites",
        Path("2d-assets") / "ui",
        Path("2d-assets") / "textures",
        Path("audio") / "sound-effects",
        Path("audio") / "music",
        "misc",
    ]
    for sub in subfolders:
        path = base_path / sub
        path.mkdir(parents=True, exist_ok=True)
    return base_path


def main() -> None:
    """Main entry point for the script.

    This script can take an optional username as a command-line argument. If a username is not
    provided via the command line, the script will prompt the user to enter one. The script
    will continue prompting until a non-empty username is provided. After creating the folder
    structure, it will wait for the user to press Enter before exiting. If input cannot be
    obtained (for example when run by double-clicking without an interactive terminal),
    it will print an error and exit gracefully.
    """
    username = None
    # Get username from command-line argument if available
    if len(sys.argv) >= 2:
        username = sys.argv[1]

    if not username:
        # Prompt for username interactively
        while True:
            try:
                username_input = input("Enter your GitHub username: ").strip()
            except (EOFError, KeyboardInterrupt):
                print(
                    "\nUnable to read input. Please run this script in a terminal or provide the username as an argument."
                )
                return
            if username_input:
                username = username_input
                break
            print("Username cannot be empty. Please try again.")

    base_path = ASSETS_ROOT / username
    create_structure(base_path)
    print(f"Asset folder structure created at '{base_path.relative_to(REPO_ROOT)}'.")

    # Pause to allow the user to read the output when run interactively
    try:
        input("\nPress Enter to exit...")
    except (EOFError, KeyboardInterrupt):
        pass


if __name__ == "__main__":
    main()
