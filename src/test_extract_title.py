import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_basic_title(self):
        self.assertEqual(extract_title("# Hello World"), "Hello World")

    def test_title_with_extra_spaces(self):
        self.assertEqual(extract_title("#    My Awesome Page   "), "My Awesome Page")

    def test_title_in_full_document(self):
        md = """# My Blog
This is the content.

## Subsection"""
        self.assertEqual(extract_title(md), "My Blog")

    def test_no_title_raises(self):
        with self.assertRaises(Exception):
            extract_title("Just some paragraph\n\nNo title here")

    def test_multiple_headings(self):
        md = """## Small heading
# Main Title
### Even smaller"""
        self.assertEqual(extract_title(md), "Main Title")


if __name__ == "__main__":
    unittest.main()