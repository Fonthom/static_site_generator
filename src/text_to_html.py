from textnode import TextNode, TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if not isinstance(text_node, TextNode):
        raise TypeError(f"Expected TextNode, got {type(text_node).__name__}")

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)

        case TextType.BOLD:
            return LeafNode("b", text_node.text)

        case TextType.ITALIC:
            return LeafNode("i", text_node.text)

        case TextType.CODE:
            return LeafNode("code", text_node.text)

        case TextType.LINK:
            if text_node.url is None:
                raise ValueError("TextNode of type LINK must have a url property")
            return LeafNode("a", text_node.text, {"href": text_node.url})

        case TextType.IMAGE:
            if text_node.url is None:
                raise ValueError("TextNode of type IMAGE must have a url property")
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

        case _:
            raise Exception(f"Invalid TextType: {text_node.text_type}")