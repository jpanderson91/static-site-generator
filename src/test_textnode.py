import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    # Two nodes with same text and type (no url) are equal
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    # Two nodes with same text, type, and url are equal
    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)

    # A node is equal to itself
    def test_eq_same_instance(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node)

    # Node with url is not equal to node without url
    def test_noteq_url_vs_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    # Nodes with different text types are not equal
    def test_noteq_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    # Nodes with different urls are not equal
    def test_noteq_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)

    # Node with url is not equal to node with explicit None url
    def test_noteq_url_none_explicit(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    # Nodes with different text are not equal
    def test_noteq_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text nod", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node, node2)
        


if __name__ == "__main__":
    unittest.main()
    
