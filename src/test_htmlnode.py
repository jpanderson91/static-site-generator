import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    # props_to_html returns correct string with multiple attributes
    def test_props_to_html_multiple(self):
        node = HTMLNode("a", "click here", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    # props_to_html returns empty string when props is None
    def test_props_to_html_none(self):
        node = HTMLNode("p", "hello")
        self.assertEqual(node.props_to_html(), "")

    # props_to_html returns correct string with single attribute
    def test_props_to_html_single(self):
        node = HTMLNode("img", None, None, {"src": "image.png"})
        self.assertEqual(node.props_to_html(), ' src="image.png"')

    # to_html raises NotImplementedError
    def test_to_html_not_implemented(self):
        node = HTMLNode("p", "hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    # repr returns expected string representation
    def test_repr(self):
        node = HTMLNode("p", "hello", None, {"class": "text"})
        self.assertEqual(repr(node), "HTMLNode(p, hello, None, {'class': 'text'})")


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just raw text")
        self.assertEqual(node.to_html(), "Just raw text")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_repr(self):
        node = LeafNode("a", "link", {"href": "https://example.com"})
        self.assertEqual(repr(node), "LeafNode(a, link, {'href': 'https://example.com'})")


if __name__ == "__main__":
    unittest.main()
