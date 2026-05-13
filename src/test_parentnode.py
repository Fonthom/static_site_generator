import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_props(self):
        node = ParentNode("div", [LeafNode("p", "hello")], {"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><p>hello</p></div>')

    def test_no_tag_raises(self):
        node = ParentNode(None, [LeafNode("p", "hello")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children_raises(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_deeply_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "p",
                            [LeafNode("b", "deep")]
                        )
                    ]
                )
            ]
        )
        self.assertEqual(node.to_html(), "<div><section><p><b>deep</b></p></section></div>")

    def test_mixed_parent_and_leaf_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "bold"),
                ParentNode("p", [LeafNode(None, "text")]),
                LeafNode("i", "italic"),
            ]
        )
        self.assertEqual(node.to_html(), "<div><b>bold</b><p>text</p><i>italic</i></div>")

if __name__ == "__main__":
    unittest.main()