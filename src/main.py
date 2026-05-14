import sys
from pathlib import Path
from copy_static import copy_static
from generate_pages import generate_pages_recursive


def main():
    print("Starting static site generation...\n")
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    root_dir = Path(__file__).parent.parent.absolute()

    copy_static()
    generate_pages_recursive(
        content_dir_path=str(root_dir / "content"),
        template_path=str(root_dir / "template.html"),
        dest_dir_path=str(root_dir / "docs"),
        basepath=basepath
    )
    print("\nStatic files copied successfully!")
    print("Site generation complete!")


if __name__ == "__main__":
    main()
