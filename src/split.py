from textnode import TextNode, TextType
from extract import extract_markdown_images, extract_markdown_links


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if delimiter not in old_node.text:
            new_nodes.append(old_node)
            continue

        parts = old_node.text.split(delimiter)

        if len(parts) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: missing closing delimiter '{delimiter}'")

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        last_end = 0

        for alt_text, url in images:
            image_markdown = f"![{alt_text}]({url})"
            start = text.find(image_markdown, last_end)

            if start == -1:
                continue

            if start > last_end:
                new_nodes.append(TextNode(text[last_end:start], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            last_end = start + len(image_markdown)

        if last_end < len(text):
            new_nodes.append(TextNode(text[last_end:], TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:

    new_nodes: list[TextNode] = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        last_end = 0

        for anchor_text, url in links:
            link_markdown = f"[{anchor_text}]({url})"
            start = text.find(link_markdown, last_end)

            if start == -1:
                continue

            if start > last_end:
                new_nodes.append(TextNode(text[last_end:start], TextType.TEXT))

            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))

            last_end = start + len(link_markdown)

        if last_end < len(text):
            new_nodes.append(TextNode(text[last_end:], TextType.TEXT))

    return new_nodes