import unittest
from textnode import TextType, TextNode
from htmlnode import LeafNode
from sndelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected)
    
    def test_bold_delimiter(self):
        # test with TextType.BOLD
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expected)
    
    def test_italic_delimiter(self):
        # test with TextType.ITALIC
        node = TextNode("This is text with a *italic* word", TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(result, expected)
    
    def test_multiple_delimited_sections(self):
        # e.g. two bold words
        node = TextNode("This has **two** bold **words** here", TextType.TEXT)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("two", TextType.BOLD),
            TextNode(" bold ", TextType.TEXT),
            TextNode("words", TextType.BOLD),
            TextNode(" here", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_delimiter_at_start(self):
        node = TextNode("**bold** text", TextType.TEXT)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_delimiter_at_end(self):
        node = TextNode("text **bold**", TextType.TEXT)
        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_non_text_node_passthrough(self):
        # a TextType.BOLD node should pass through unchanged
        node = TextNode("bold", TextType.BOLD)
        expected = [TextNode("bold", TextType.BOLD)]
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_mixed_list(self):
        # text and non-text nodes together
        node1 = TextNode("This is text with a **bold** word", TextType.TEXT)
        node2 = TextNode("This is also **bold**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
            TextNode("This is also **bold**", TextType.BOLD),
        ]
        result = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_unclosed_delimiter(self):
        # should raise ValueError
        node = TextNode("This is text with a **bold word", TextType.TEXT)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], "**", TextType.BOLD)

    def test_no_delimiters(self):
        # plain text returns as-is
        node = TextNode("This is text with no delimiters", TextType.TEXT)
        expected = [TextNode("This is text with no delimiters", TextType.TEXT)]
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        # empty string between delimiters gets skipped
        node = TextNode("This is text with a **** word", TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode(" word", TextType.TEXT),
            ]

        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, expected)


