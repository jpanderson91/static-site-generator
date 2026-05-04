# Create an extract_title(markdown) function.
# It should pull the h1 header from the markdown file (the line that starts with a single #) and return it.
# If there is no h1 header, raise an exception.
# extract_title("# Hello") should return "Hello" (strip the # and any leading or trailing whitespace) 
def extract_title(markdown):
    """Extract the h1 header from markdown text."""
    lines = markdown.split('\n')
    
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('# ') and not stripped_line.startswith('## '):
            return stripped_line[2:].strip()
        elif stripped_line == '#':
            return ''
    
    raise ValueError("No h1 header found in markdown")