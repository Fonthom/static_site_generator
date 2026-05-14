import os
from markdown_to_html import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str = "/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    title = extract_title(markdown_content)

    full_html = template.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    if basepath != "/":
        normalized_basepath = basepath if basepath.endswith("/") else f"{basepath}/"
        full_html = full_html.replace('href="/', f'href="{normalized_basepath}')
        full_html = full_html.replace('src="/', f'src="{normalized_basepath}')
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Page generated successfully at {dest_path}")