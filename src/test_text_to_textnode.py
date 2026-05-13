import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):

    def test_full_markdown_example(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        
        new_nodes = text_to_textnodes(text)
        
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        
        self.assertListEqual(expected, new_nodes)

    def test_plain_text(self):
        nodes = text_to_textnodes("Just plain text")
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], TextNode("Just plain text", TextType.TEXT))

    def test_only_bold(self):
        nodes = text_to_textnodes("This is **bold** text")
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[1], TextNode("bold", TextType.BOLD))

    def test_only_image(self):
        nodes = text_to_textnodes("Here is an ![image](https://example.com/img.png)")
        self.assertEqual(nodes[0], TextNode("Here is an ", TextType.TEXT))
        self.assertEqual(nodes[1], TextNode("image", TextType.IMAGE, "https://example.com/img.png"))

    def test_only_link(self):
        nodes = text_to_textnodes("Check out [boot.dev](https://boot.dev)")
        self.assertEqual(nodes[1], TextNode("boot.dev", TextType.LINK, "https://boot.dev"))

    def test_empty_string(self):
        nodes = text_to_textnodes("")
        self.assertEqual(nodes, [TextNode("", TextType.TEXT)])

    def test_mixed_complex(self):
        text = "**Bold** and *italic* with `code` and ![img](img.png) and [link](url.com)"
        nodes = text_to_textnodes(text)
        self.assertGreater(len(nodes), 5)


if __name__ == "__main__":
    unittest.main()