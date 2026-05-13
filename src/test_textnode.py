import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("click here", TextType.LINK, "https://boot.dev")
        node2 = TextNode("click here", TextType.LINK, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_different_text_type(self):
        node = TextNode("hello", TextType.BOLD)
        node2 = TextNode("hello", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_different_text(self):
        node = TextNode("hello", TextType.TEXT)
        node2 = TextNode("world", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_url_none_by_default(self):
        node = TextNode("hello", TextType.TEXT)
        self.assertIsNone(node.url)

    def test_url_none_not_equal_to_url(self):
        node = TextNode("hello", TextType.LINK)
        node2 = TextNode("hello", TextType.LINK, "https://boot.dev")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
