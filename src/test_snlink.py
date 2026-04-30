import unittest
from textnode import TextType, TextNode
from snlink import split_nodes_link

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode("This is text with a [link](https://www.scaler.com) and [another link](https://www.google.com)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.scaler.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("another link", TextType.LINK, "https://www.google.com")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_multi(self):
        node = TextNode("This is text with a [link](https://www.scaler.com) and [another link](https://www.google.com) and [one more](https://www.github.com)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.scaler.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("another link", TextType.LINK, "https://www.google.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("one more", TextType.LINK, "https://www.github.com")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_not_texttype(self):
        node = TextNode("This is text with a [link](https://www.scaler.com) and [another link](https://www.google.com)", TextType.BOLD)
        result = split_nodes_link([node])
        expected = [
            TextNode("This is text with a [link](https://www.scaler.com) and [another link](https://www.google.com)", TextType.BOLD)
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_empty(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [TextNode("", TextType.TEXT)]
        self.assertEqual(result, expected)
        
    def test_link_at_start(self):
        node = TextNode("[link](https://www.scaler.com) is a website", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("link", TextType.LINK, "https://www.scaler.com"),
            TextNode(" is a website", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_link_at_end(self):
        node = TextNode("This is a website [link](https://www.scaler.com)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("This is a website ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.scaler.com"),
        ]
        self.assertEqual(result, expected)

    def test_single_link_no_surrounding_text(self):
        node = TextNode("[link](https://www.scaler.com)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("link", TextType.LINK, "https://www.scaler.com"),
        ]
        self.assertEqual(result, expected)

    def test_multiple_links_back_to_back_no_text_between(self):
        node = TextNode("[link1](https://www.scaler.com)[link2](https://www.google.com)", TextType.TEXT)
        result = split_nodes_link([node])
        expected = [
            TextNode("link1", TextType.LINK, "https://www.scaler.com"),
            TextNode("link2", TextType.LINK, "https://www.google.com"),
        ]
        self.assertEqual(result, expected)

    def test_mix_of_text_non_text_nodes_in_input_list(self):
        text_node = TextNode("This is text with a [link](https://www.scaler.com)", TextType.TEXT)
        bold_node = TextNode("This is bold", TextType.BOLD)
        result = split_nodes_link([text_node, bold_node])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.scaler.com"),
            TextNode("This is bold", TextType.BOLD)
        ]
        self.assertEqual(result, expected)



