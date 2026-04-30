# Our grug-brain static site generator only cares about two things:

# Inline markdown
# Block markdown
# Inline markdown is what we just took care of. It's the stuff that's inside of a block.

# Block-level markdown is just the separation of different sections of an entire document. 
# In well-written markdown (which we'll just assume is the only thing going into our generator)
# blocks are separated by a single blank line. Here are 3 distinct blocks:

# This is a heading

# This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

# - This is the first list item in a list block
# - This is a list item
# - This is another list item

# create a new function called markdown_to_blocks(markdown). It takes a raw markdown string
# (representing a full document) as input and returns a list of "block" strings. 
# The example above would be split into these three strings:
# This is a heading
# This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
# - This is the first list item in a list block
# - This is a list item
# - This is another list item
# The .split() method can be used to split a string into blocks based on a delimiter (\n\n is a double newline).
# You should .strip() any leading or trailing whitespace from each block.
# Remove any "empty" blocks due to excessive newlines.

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    result = []
    for block in blocks:
        block = block.strip()
        if block:
            result.append(block)
    return result
