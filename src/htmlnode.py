# define a class called HTMLNode
# The HTMLNode class should have 4 data members set in the constructor:
# tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
# value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
# children - A list of HTMLNode objects representing the children of this node
# props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
# every data member should be optional and default to None:

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

# An HTMLNode without a tag will just render as raw text
# An HTMLNode without a value will be assumed to have children
# An HTMLNode without children will be assumed to have a value
# An HTMLNode without props simply won't have any attributes

# Add a to_html(self) method. For now, it should just raise a NotImplementedError. Child classes will override this method to render themselves as hTML.
    def to_html(self):
        raise NotImplementedError
# Add a props_to_html(self) method. It should return a formatted string representing the HTML attributes of the node. For example, if self.props is:  
#{
#    "href": "https://www.google.com",
#    "target": "_blank",
#}
# Then self.props_to_html() should return:
#  href="https://www.google.com" target="_blank"
# Notice the leading space character before href and before target. This is important. HTML attributes are always separated by spaces. If self.props is None or empty, return an empty string.

    def props_to_html(self):
        if self.props is None:
            return ""
        props_string = ""
        for key, value in self.props.items():
            props_string += f' {key}="{value}"'
        return props_string

# Add a __repr__(self) method. Give yourself a way to print an HTMLNode object and see its tag, value, children, and props. This will be useful for your debugging.
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf node must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


