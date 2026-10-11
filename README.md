# file-org-system-.
# 📂 Automated File Organizer Script

A handy automation script built in **Python** that scans a target folder (like your messy Downloads or Desktop) and systematically sorts files into appropriate subfolders based on their extensions. Designed for real-world desktop cleanup and workflow automation[cite: 1].

## ✨ Features
* **Extension-Based Sorting:** Automatically categorizes files into structured folders such as *Images, Documents, Videos, Music, Archives, Code, and Executables*.
* **Collision Handling:** Safely renames incoming files (using numeric suffixes) if a file with the exact same name already exists in the destination folder.
* **Dry-Run Mode:** Simulate the organization process (`--dry-run`) to see what changes will happen without actually moving any files[cite: 1].
* **Activity Logging:** Generates detailed timestamped logs (`organizer.log`) of every file moved or processed.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Modules Used:** `os`, `shutil`, `argparse`, `datetime`[cite: 1].

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/file-organizer-script.git](https://github.com/YOUR_USERNAME/file-organizer-script.git)
