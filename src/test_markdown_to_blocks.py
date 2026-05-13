import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_multiple_empty_lines(self):
        md = "Block 1\n\n\n\nBlock 2\n\n\n\n\nBlock 3"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block 1", "Block 2", "Block 3"])

    def test_heading_and_paragraph(self):
        md = "# This is a heading\n\nThis is a paragraph.\n\n- List item 1\n- List item 2"
        blocks = markdown_to_blocks(md)
        self.assertEqual(len(blocks), 3)
        self.assertTrue(blocks[0].startswith("#"))
        self.assertTrue(blocks[2].startswith("-"))

    def test_empty_input(self):
        self.assertEqual(markdown_to_blocks(""), [])
        self.assertEqual(markdown_to_blocks("\n\n\n"), [])

    def test_block_with_leading_trailing_whitespace(self):
        md = "   This has leading spaces   \n\n   And this too   "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "This has leading spaces",
            "And this too"
        ])

    def test_single_block(self):
        md = "Just one block of text"
        self.assertEqual(markdown_to_blocks(md), ["Just one block of text"])


if __name__ == "__main__":
    unittest.main()