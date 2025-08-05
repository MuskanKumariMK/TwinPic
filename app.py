import hashlib
from PIL import Image
import streamlit as st
import io


# Function to calculate hash of an image file
def get_image_hash(image_bytes):
    try:
        return hashlib.md5(image_bytes).hexdigest()
    except Exception:
        return None


# App UI
st.set_page_config(page_title="TwinPic - Duplicate Image Finder", layout="wide")
st.title("TwinPic: Duplicate Image Finder")

# File uploader for multiple images
uploaded_files = st.file_uploader(
    "Upload image files to check for duplicates",
    type=["png", "jpg", "jpeg", "bmp", "gif"],
    accept_multiple_files=True,
)

if uploaded_files:
    hash_dict = {}
    duplicates = {}

    for file in uploaded_files:
        image_bytes = file.read()
        image_hash = get_image_hash(image_bytes)

        if not image_hash:
            continue

        if image_hash in hash_dict:
            if image_hash not in duplicates:
                duplicates[image_hash] = [hash_dict[image_hash]]
            duplicates[image_hash].append((file.name, image_bytes))
        else:
            hash_dict[image_hash] = (file.name, image_bytes)

    if duplicates:
        st.markdown("### Duplicate Images Found:")
        for hash_val, dup_group in duplicates.items():
            st.markdown("---")
            st.subheader("Duplicate Group")
            cols = st.columns(len(dup_group))
            for idx, (filename, img_bytes) in enumerate(dup_group):
                with cols[idx]:
                    try:
                        image = Image.open(io.BytesIO(img_bytes))
                        st.image(image, caption=filename, use_container_width=True)
                    except:
                        st.warning(f"Unable to display image: {filename}")
    else:
        st.success("No duplicate images found.")
