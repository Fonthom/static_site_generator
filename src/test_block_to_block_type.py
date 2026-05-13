import unittest
from block_type import BlockType
from block_to_block_type import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("### Heading 3"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_code_block(self):
        block = "```\ndef hello():\n    print('hi')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> This is a quote\n> Another line of quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- First item\n- Second item\n- Third item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("Just a normal paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("This has **bold** and _italic_"), BlockType.PARAGRAPH)

    def test_edge_cases(self):
        self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("1. Only one item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("- Item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("> Single quote line"), BlockType.QUOTE)

    def test_invalid_ordered_list(self):
        block = "1. First\n3. Skipped two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_heading_without_space(self):
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()