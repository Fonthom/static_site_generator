import os
from pathlib import Path
from generate_page import generate_page


def generate_pages_recursive(content_dir_path: str, template_path: str, dest_dir_path: str):
    content_path = Path(content_dir_path)
    dest_path = Path(dest_dir_path)

    print(f"Generating pages from '{content_path}' to '{dest_path}'...\n")

    for root, dirs, files in os.walk(content_path):
        for file in files:
            if file.endswith(".md"):
                md_file_path = os.path.join(root, file)
                rel_path = os.path.relpath(root, content_path)
                if rel_path == ".":
                    html_dir = dest_path
                else:
                    html_dir = dest_path / rel_path

                html_file_name = file.replace(".md", ".html")
                html_file_path = html_dir / html_file_name

                html_dir.mkdir(parents=True, exist_ok=True)
                generate_page(
                    from_path=md_file_path,
                    template_path=template_path,
                    dest_path=str(html_file_path)
                )

    print("\n✅ All pages generated successfully!")