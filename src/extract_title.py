def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            # Remove "# " and strip whitespace
            title = stripped[2:].strip()
            return title
    
    raise Exception("No h1 header found in markdown file")