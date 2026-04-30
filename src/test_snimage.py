import unittest
from textnode import TextType, TextNode
from snimage import split_nodes_image

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                   "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
          ],
         new_nodes,
         )
    
    def test_no_images_in_text(self):
        node = TextNode("This is text with no images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])

    def test_image_at_start(self):
        node = TextNode(
            "![image1](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://i.imgur.com/3elNhQu.png) are here",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" are here", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_image_at_end(self):
        node = TextNode(
            "Here is some text ![image1](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Here is some text ", TextType.TEXT),
                TextNode("image1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_single_image_no_surrounding_text(self):
        node = TextNode("![alt text](https://example.com/image.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
            ],
            new_nodes,
        )

    def test_multiple_images_back_to_back_no_text_between(self):
        node = TextNode(
            "![img1](https://example.com/img1.png)![img2](https://example.com/img2.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("img1", TextType.IMAGE, "https://example.com/img1.png"),
                TextNode("img2", TextType.IMAGE, "https://example.com/img2.png"),
            ],
            new_nodes,
        )

    def test_non_text_node_passed_in(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])

    def test_mix_text_non_text_nodes_in_input_list(self):
        text_node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT)
        bold_node = TextNode("This is bold text", TextType.BOLD)
        new_nodes = split_nodes_image([text_node, bold_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("This is bold text", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_empty_string_text_node(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(new_nodes, [node])


    