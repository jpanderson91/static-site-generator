import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Just text"),
                LeafNode("i", "italic text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Just text<i>italic text</i></p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_many_children(self):
            children = [
                LeafNode("p", "Hello"),
                LeafNode(None, " "),
                LeafNode("p", "world"),
            ]
            parent = ParentNode("div", children)
            self.assertEqual(
                parent.to_html(),
                "<div><p>Hello</p> <p>world</p></div>",
            )
    
    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "hello")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_empty_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_to_html_with_props(self):
        node = ParentNode("div", [LeafNode("p", "hello")], {"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><p>hello</p></div>')

    def test_repr(self):
                node = ParentNode("div", [LeafNode("p", "hello")], {"class": "container"})
                self.assertEqual(repr(node), "ParentNode(div, [LeafNode(p, hello, None)], {'class': 'container'})")   

if __name__ == "__main__":
    unittest.main()
