# Create a generate_page(from_path, template_path, dest_path) function. It should:
# Print a message like "Generating page from from_path to dest_path using template_path".
# Read the markdown file at from_path and store the contents in a variable.
# Read the template file at template_path and store the contents in a variable.
# Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
# Use the extract_title function to grab the title of the page.
# Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
# Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.

from markdown_to_blocks import markdown_to_html_node
from extract_title import extract_title

import os
def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    title = extract_title(markdown_content)

    final_content = template_content.replace('{{ Title }}', title)
    final_content = final_content.replace('{{ Content }}', html_content)
    # Replace root-relative paths with the configured basepath
    final_content = final_content.replace('href="/', f'href="{basepath}')
    final_content = final_content.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(final_content)
