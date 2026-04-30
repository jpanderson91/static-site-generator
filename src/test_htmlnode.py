import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
