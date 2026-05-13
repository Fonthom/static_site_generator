import unittest
from extract import extract_markdown_images, extract_markdown_links


class TestMarkdownExtractors(unittest.TestCase):

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
        self.assertListEqual(expected, matches)

    def test_extract_single_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_no_images(self):
        self.assertListEqual([], extract_markdown_images("Just plain text no images"))

    def test_image_with_special_chars(self):
        text = "Check this out: ![alt text with (parentheses) & more](https://example.com/image.png)"
        expected = [("alt text with (parentheses) & more", "https://example.com/image.png")]
        self.assertListEqual(expected, extract_markdown_images(text))

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        self.assertListEqual(expected, matches)

    def test_no_links(self):
        self.assertListEqual([], extract_markdown_links("No links here at all"))

    def test_mixed_images_and_links(self):
        text = "See this image ![cat](cat.jpg) and this link [boot.dev](https://boot.dev)"
        self.assertEqual(len(extract_markdown_images(text)), 1)
        self.assertEqual(len(extract_markdown_links(text)), 1)


if __name__ == "__main__":
    unittest.main()