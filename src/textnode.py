from htmlnode import LeafNode
from enum import Enum

class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"
    

    
class TextNode:
    
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    # __eq__ method compares self to another TextNode instance(other) and returns True if all of their properties are equal. Out future unit tests will rely on this method to compare objects.
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    # __repr__ method that returns a string representation of the TextNode object. It should look like this:
    # TextNode(TEXT, TEXT_TYPE, URL)
    # Where TEXT, TEXT_TYPE, and URL are the values of the text, text_type, and url properties, respectively.
    # You can get the string representation of the text_type enum by using the .value field.
    
    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type.value!r}, {self.url!r})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"invalid text type: {text_node.text_type}")


