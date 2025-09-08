[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-blue?logo=streamlit)](https://streamlit.io)

# TwinPic: Duplicate Image Finder & Deleter


TwinPic is a **Streamlit-powered web application** that scans a folder, identifies duplicate images using **MD5 hashing**, and allows you to delete them easily.  
This helps in keeping your photo library clean and organized.

---

## ✨ Features
- 📂 Scan any folder and its subfolders for image files.
- 🔑 Generate unique **MD5 hash** for each image to detect duplicates.
- 🖼️ Display duplicate images side by side for comparison.
- 🗑️ Delete unwanted duplicate images directly from the UI.
- ⚡ Simple, fast, and lightweight app with an interactive **Streamlit interface**.

---

## 🛠️ Tech Stack
- **Python**  
- **Streamlit** – for building the interactive UI  
- **Pillow (PIL)** – for image handling  
- **Hashlib** – for generating MD5 hashes  
- **OS / Pathlib** – for file system operations  

---

## How to Setup & Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/MuskanKumariMK/TwinPic.git
   cd TwinPic
   ```
2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
venv\Scripts\activate  # on Windows

```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. RUn the App

```bash
streamlit run main.py

```
