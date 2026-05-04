from textnode import TextType, TextNode
from sndelimiter import split_nodes_delimiter
from snimage import split_nodes_image
from snlink import split_nodes_link

def text_to_textnodes(text):
    # Start with a single node containing the entire text
    initial_node = [TextNode(text, TextType.TEXT)]
    
    # Apply each splitting function in sequence
    # Splitting bold text
    bold_split = split_nodes_delimiter(initial_node, "**", TextType.BOLD)
    italic_split = split_nodes_delimiter(bold_split, "*", TextType.ITALIC)
    italic_split = split_nodes_delimiter(italic_split, "_", TextType.ITALIC)
    code_split = split_nodes_delimiter(italic_split, "`", TextType.CODE)
    image_split = split_nodes_image(code_split)
    return split_nodes_link(image_split)
