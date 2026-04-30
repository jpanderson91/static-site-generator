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
    
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
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


