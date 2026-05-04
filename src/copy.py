# Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
# It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
# It should copy all files and subdirectories, nested files, etc.
# I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.
import os
import shutil
import logging

# Deletes all files and subdirectories inside the given directory, leaving the directory itself intact
def clear_directory(directory_path):
    """Delete all contents of the specified directory."""
    if os.path.exists(directory_path):
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                
                os.remove(item_path)
                
        logging.info(f"Cleared directory: {directory_path}")

# Copies a single file from source to destination, preserving metadata
def copy_file(src_file, dest_file):
    """Copy a single file from source to destination."""
    shutil.copy2(src_file, dest_file)
    logging.info(f"Copied file: {src_file} -> {dest_file}")

# Walks through the source directory, recreating subdirectories and copying files into the destination
def copy_directory_recursive(src_dir, dest_dir):
    """Recursively copy all contents from source to destination directory."""
    
    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        if os.path.isdir(src_path):
            os.makedirs(dest_path, exist_ok=True)
            copy_directory_recursive(src_path, dest_path)
        else:
            copy_file(src_path, dest_path)

# Entry point: clears the public directory, then copies everything from static into it
def copy_static_to_public(static_dir="static", public_dir="public"):
    """Copy all contents from static directory to public directory."""
    logging.basicConfig(level=logging.INFO)
    clear_directory(public_dir)
    os.makedirs(public_dir, exist_ok=True)

    if os.path.exists(static_dir):
        copy_directory_recursive(static_dir, public_dir)
        logging.info(f"Successfully copied {static_dir} to {public_dir}")
    else:
        logging.warning(f"Source directory {static_dir} does not exist")
        