from textnode import TextType, TextNode
from sndelimiter import split_nodes_delimiter
from snimage import split_nodes_image
from snlink import split_nodes_link


#Time to put all the "splitting" functions together into a function that can convert a raw string of markdown-flavored text into a list of TextNode objects.
#example input This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
# # example output list of nodes:
# [
#     TextNode("This is ", TextType.TEXT),
#     TextNode("text", TextType.BOLD),
#     TextNode(" with an ", TextType.TEXT),
#     TextNode("italic", TextType.ITALIC),
#     TextNode(" word and a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" and an ", TextType.TEXT),
#     TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
#     TextNode(" and a ", TextType.TEXT),
#     TextNode("link", TextType.LINK, "https://boot.dev"),
# ]

def text_to_textnodes(text):
    # Start with a single node containing the entire text
    initial_node = [TextNode(text, TextType.TEXT)]
    
    # Apply each splitting function in sequence
    # Splitting bold text
    bold_split = split_nodes_delimiter(initial_node, "**", TextType.BOLD)
    italic_split = split_nodes_delimiter(bold_split, "*", TextType.ITALIC)
    code_split = split_nodes_delimiter(italic_split, "`", TextType.CODE)
    image_split = split_nodes_image(code_split)
    return split_nodes_link(image_split)
