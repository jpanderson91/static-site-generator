# hello world
# create a main() function in main.py and call it. The function should create a new TextNode object with some dummy values. 
# Print the object, and make sure it looks like you'd expect. For example:
# TextNode(This is some anchor text, link, https://www.boot.dev)
def main():
    from textnode import TextNode
    from textnode import Bender
    from copy import copy_static_to_public

    copy_static_to_public()

    node = TextNode("This is some anchor text", Bender.WATER_BENDER, "https://www.boot.dev")
    print(node)

main()