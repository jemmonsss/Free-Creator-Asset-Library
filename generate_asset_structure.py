# generate_asset_structure.py

This Python script creates the recommended asset folder structure for a contributor.

```python
#!/usr/bin/env python3
"""generate_asset_structure.py

This script creates the recommended asset folder structure for a contributor.

Usage:
    python generate_asset_structure.py <github_username>

If no username is provided, the script will prompt for one.

The structure created is:
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
"""
import os
import sys


def create_structure(base_path):
    """Create the folder structure given a base path."""
    subfolders = [
        os.path.join("3d-assets", "models"),
        os.path.join("3d-assets", "materials"),
        os.path.join("3d-assets", "scenes"),
        os.path.join("2d-assets", "sprites"),
        os.path.join("2d-assets", "ui"),
        os.path.join("2d-assets", "textures"),
        os.path.join("audio", "sound-effects"),
        os.path.join("audio", "music"),
        "misc",
    ]
    for sub in subfolders:
        path = os.path.join(base_path, sub)
        os.makedirs(path, exist_ok=True)
    return base_path


def main():
    """Main entry point for the script."""
    if len(sys.argv) >= 2:
        username = sys.argv[1]
    else:
        username = input("Enter your GitHub username: ").strip()
    if not username:
        print("Username cannot be empty.")
        sys.exit(1)
    base_path = os.path.join("assets", username)
    create_structure(base_path)
    print(f"Folder structure created at {base_path}")


if __name__ == "__main__":
    main()
```
