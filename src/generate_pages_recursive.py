# it should Crawl every entry in the content directory
# For each markdown file found, generate a new .html file using the same template.html. The generated pages should be written to the public directory in the same directory structure.
import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Loop through all items in the current content directory
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        # If the item is a directory, recurse into it with the matching destination subdirectory
        if os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, os.path.join(dest_dir_path, item))
        # If the item is a markdown file, generate the corresponding HTML page
        elif item.endswith(".md"):
            dest_path = os.path.join(dest_dir_path, item.replace(".md", ".html"))
            generate_page(src_path, template_path, dest_path)
