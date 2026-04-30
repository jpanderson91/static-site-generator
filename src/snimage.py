from textnode import TextType, TextNode
from extract_links import extract_markdown_images
# Now that we have the extraction functions, we will need to be able to split raw markdown text into TextNodes based on images and links
# They should behave very similarly to split_nodes_delimiter, but obviously don't need a delimiter or a text type as input, because they always operate on images or links respectively. Here's some example usage:

# # node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_link([node])
# # [
# #     TextNode("This is text with a link ", TextType.TEXT),
# #     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
# #     TextNode(" and ", TextType.TEXT),
# #     TextNode(
# #         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
# #     ),
# # ]



def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        image_text = old_node.text
        images = extract_markdown_images(image_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        
        for i, image in enumerate(images):
            parts = image_text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
            if len(parts) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            image_text = parts[1]
        if image_text != "":
            new_nodes.append(TextNode(image_text, TextType.TEXT))
    return new_nodes
    