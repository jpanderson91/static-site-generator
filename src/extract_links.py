import re
from textnode import TextType, TextNode
from htmlnode import LeafNode

# images
# r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

# regular links
# r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)   