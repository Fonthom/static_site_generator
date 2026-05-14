import os
import shutil
from pathlib import Path


def copy_static(src_dir: str = "../static", dest_dir: str = "../public"):
    """Recursively copy static/ directory to public/"""
    root_dir = Path(__file__).parent.parent.absolute()
    source_path = root_dir / "static"
    dest_path = root_dir / "docs"

    # Clean destination
    if dest_path.exists():
        shutil.rmtree(dest_path)
        print(f"🗑️  Deleted existing '{dest_path.name}' directory")

    # Create fresh public directory
    dest_path.mkdir(parents=True, exist_ok=True)
    print(f"📁 Created '{dest_path.name}' directory")

    # Copy all files recursively
    for root, dirs, files in os.walk(source_path):
        rel_path = os.path.relpath(root, source_path)
        dest_root = dest_path / rel_path

        if rel_path != ".":
            dest_root.mkdir(parents=True, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = dest_root / file
            shutil.copy2(src_file, dest_file)
            print(f"✅ Copied: {file}")

    print("🎉 Static files copied successfully!\n")