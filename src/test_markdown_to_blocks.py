import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_excessive_newlines(self):
        md = "block one\n\n\n\nblock two\n\n\n\n\nblock three"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["block one", "block two", "block three"])

    def test_whitespace_stripping(self):
        md = "  hello  \n\n  world  "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["hello", "world"])

    def test_single_block(self):
        md = "just one block"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["just one block"])

    def test_empty_string(self):
        blocks = markdown_to_blocks("")
        self.assertEqual(blocks, [])

    def test_only_whitespace(self):
        blocks = markdown_to_blocks("   \n\n   \n\n   ")
        self.assertEqual(blocks, [])
