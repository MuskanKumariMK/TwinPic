import os  # Interact my Os for folder and file operations delete the files and reads the files or images
import hashlib  # It genereate the uniques hash for each image using MD5 algorithm
from PIL import Image  # Pillow library to handle image files
import streamlit as st  # Straemlit for web app interface
from pathlib import Path  # Pathlib for file path manipulations

# Function to calculate hash


def get_image_hash(file_path):
    try:
        with open(file_path, "rb") as f:  # Open the file in binary mode
            return hashlib.md5(
                f.read()
            ).hexdigest()  # Read the file and generate MD5 hash
    except Exception as e:
        return None


# -------- UI of the App --------
# App Title
st.set_page_config(page_title="TwinPic - Duplicate Image Finder", layout="wide")
st.title(" TwinPic: Duplicate Image Finder & Deleter")

# Folder Input
folder_path = st.text_input(
    " Enter the folder path to scan:", placeholder="e.g., C:/MyPhotos"
)

# Main Logic

if folder_path and os.path.isdir(folder_path):  # Check if the folder path is valid
    hash_dict = {}  # Dictionary to store file hashes
    duplicates = {}  # Dictionary to store duplicate files

    # Walk through all files in folder and subfolders
    for root, dirs, files in os.walk(
        folder_path
    ):  # Traverse through the directory tree
        for file in files:  # Iterate through each file
            # Check if the file is an image based on its extension
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                # Construct full file path
                full_path = os.path.join(root, file)
                # Get the image hash
                file_hash = get_image_hash(full_path)
                # If hash is None, skip the file
                # This can happen if the file is not readable or is corrupted
                if not file_hash:
                    continue
                # Check if the hash already exists in the dictionary
                if file_hash in hash_dict:
                    # If this hash is not yet in the duplicates dictionary, create a new list
                    # Start the list with the first file path that had this hash (from hash_dict)
                    if file_hash not in duplicates:
                        duplicates[file_hash] = [hash_dict[file_hash]]
                        # Add the current file path to the duplicates list for this hash
                    duplicates[file_hash].append(full_path)
                else:
                    # If this hash is seen for the first time, store its file path in hash_dict
                    hash_dict[file_hash] = full_path

    # Show Duplicates
    if duplicates:  # If any duplicates were found
        st.markdown("Duplicate Images Found")
        # Loop through each group of duplicates (images with the same hash)
        for hash_val, dup_group in duplicates.items():
            st.markdown("---")
            st.subheader("Duplicate Group")
            # Create columns for each duplicate image
            # This allows displaying multiple images side by side
            cols = st.columns(len(dup_group))
            # Loop through each duplicate image path
            # Display the image and a delete button for each
            for idx, dup_path in enumerate(dup_group):
                # Place each image in its own column
                with cols[idx]:
                    try:
                        # Display the image with its filename as caption
                        st.image(
                            dup_path,
                            caption=Path(dup_path).name,
                            use_container_width=True,
                        )
                        # Show a delete button below the image
                        if st.button(" Delete", key=dup_path):
                            try:
                                # Delete the file if the button is clicked
                                os.remove(dup_path)
                                st.success(f" Deleted: {dup_path}")
                            except Exception as e:
                                st.error(f" Error deleting {dup_path}: {e}")
                    except:
                        st.warning(f" Unable to load image: {dup_path}")
    else:
        st.success(" No duplicate images found.")
elif folder_path:
    st.error(" Invalid folder path.")
