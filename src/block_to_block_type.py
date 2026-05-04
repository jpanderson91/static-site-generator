import re
from markdown_to_blocks import BlockType


def block_to_block_type(text):
    lines = text.splitlines()
    
    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING
        
    if len(lines) >= 2 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
        
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
        
    if all(line.startswith("- ") for line in lines):
        return BlockType.ULIST
        
    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, 1)):
        return BlockType.OLIST
        
    return BlockType.PARAGRAPH
