from textnode import TextNode, TextType
from parentnode import ParentNode
from block_type import BlockType
from block_to_block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node

def text_to_children(text: str):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.HEADING:
            children.append(_heading_to_html(block))
        elif block_type == BlockType.CODE:
            children.append(_code_to_html(block))
        elif block_type == BlockType.QUOTE:
            children.append(_quote_to_html(block))
        elif block_type == BlockType.UNORDERED_LIST:
            children.append(_unordered_list_to_html(block))
        elif block_type == BlockType.ORDERED_LIST:
            children.append(_ordered_list_to_html(block))
        else:  
            children.append(_paragraph_to_html(block))

    return ParentNode("div", children)


def _heading_to_html(block: str) -> ParentNode:
    level = 0
    while block[level] == "#":
        level += 1
    text = block[level:].strip()
    return ParentNode(f"h{level}", text_to_children(text))


def _code_to_html(block: str) -> ParentNode:
    lines = block.splitlines()
    code_content = "\n".join(lines[1:-1])
    if code_content and not code_content.endswith("\n"):
        code_content += "\n"
    text_node = TextNode(code_content, TextType.TEXT)
    return ParentNode("pre", [ParentNode("code", [text_node_to_html_node(text_node)])])


def _quote_to_html(block: str) -> ParentNode:
    lines = block.split("\n")
    cleaned = [line.lstrip(">").strip() for line in lines]
    return ParentNode("blockquote", text_to_children("\n".join(cleaned)))


def _unordered_list_to_html(block: str) -> ParentNode:
    lines = block.split("\n")
    items = [ParentNode("li", text_to_children(line.lstrip("-").strip())) for line in lines]
    return ParentNode("ul", items)


def _ordered_list_to_html(block: str) -> ParentNode:
    lines = block.split("\n")
    items = [ParentNode("li", text_to_children(line.split(".", 1)[1].strip())) for line in lines]
    return ParentNode("ol", items)


def _paragraph_to_html(block: str) -> ParentNode:
    text = " ".join(line.strip() for line in block.split("\n") if line.strip())
    return ParentNode("p", text_to_children(text))