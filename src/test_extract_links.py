import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from extract_links import extract_markdown_images, extract_markdown_links

class TestExtractLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![cat](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("cat", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_no_images(self):
        matches = extract_markdown_images(
            "This is text with no images"
            )
        self.assertListEqual([], matches)

    def test_empty_alt_text(self):
        matches = extract_markdown_images(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_image_mixed_with_link(self):
        # should only extract the image not the link
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
            )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [link2](https://i.imgur.com/zjjcJKZ.png)"
            )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png"), ("link2", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_no_links(self):
        matches = extract_markdown_links(
            "This is text with no links"
            )
        self.assertListEqual([], matches)

    def test_link_mixed_with_image(self):
        # should only extract the link not the image
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and a ![image](https://boot.dev)"
            )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

        