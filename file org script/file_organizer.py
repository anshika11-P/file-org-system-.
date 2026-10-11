import os
import shutil
import argparse
from datetime import datetime

def organize_folder(target_dir, dry_run=False, log_file="organizer.log"):
    if not os.path.exists(target_dir):
        print(f"❌ Error: The directory '{target_dir}' does not exist.")
        return

    # Extension mapping dictionary to categorize files
    extension_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.csv', '.rtf'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv'],
        'Music': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.json', '.sql'],
        'Executables': ['.exe', '.msi', '.dmg', '.sh', '.bat']
    }

    def log_action(message):
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_msg = f"{timestamp} {message}"
        print(log_msg)
        if not dry_run:
            try:
                with open(log_file, "a") as f:
                    f.write(log_msg + "\n")
            except Exception as e:
                print(f"⚠️ Could not write to log file: {e}")

    if dry_run:
        print("\n🔍 [DRY-RUN MODE ENABLED] No actual file moves will be performed.\n")

    files_moved_count = 0

    # Scan the target directory
    try:
        items = os.listdir(target_dir)
    except Exception as e:
        print(f"❌ Error reading directory: {e}")
        return

    for item in items:
        item_path = os.path.join(target_dir, item)

        # Skip directories and the log file itself
        if os.path.isdir(item_path) or item == log_file:
            continue

        # Get file extension
        _, ext = os.path.splitext(item)
        ext = ext.lower()

        if not ext:
            category = "Others"
        else:
            category = "Others"
            for cat, extensions in extension_map.items():
                if ext in extensions:
                    category = cat
                    break

        # Define destination category folder
        category_folder = os.path.join(target_dir, category)
        destination_path = os.path.join(category_folder, item)

        # Handle name collisions
        if os.path.exists(destination_path):
            base_name, extension = os.path.splitext(item)
            counter = 1
            while True:
                new_filename = f"{base_name}_{counter}{extension}"
                destination_path = os.path.join(category_folder, new_filename)
                if not os.path.exists(destination_path):
                    break
                counter += 1

        # Perform move or log dry-run
        if dry_run:
            log_action(f"[DRY-RUN] Would move: '{item}' ➔ '{category}/'")
        else:
            try:
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                shutil.move(item_path, destination_path)
                log_action(f"Successfully moved: '{item}' ➔ '{category}/'")
                files_moved_count += 1
            except Exception as e:
                log_action(f"❌ Error moving '{item}': {e}")

    print("\n" + "=" * 40)
    print(f"🎉 Organization Complete! Total files processed: {files_moved_count}")
    if not dry_run:
        print(f"📝 Logs have been saved to '{log_file}'")
    print("=" * 40)

def main():
    parser = argparse.ArgumentParser(description="Automated File Organizer Script")
    parser.add_argument("path", type=str, help="Path to the directory you want to organize")
    parser.add_argument("--dry-run", action="store_true", help="Simulate the organization without moving files")
    parser.add_argument("--log", type=str, default="organizer.log", help="Custom log filename")

    args = parser.parse_args()
    organize_folder(target_dir=args.path, dry_run=args.dry_run, log_file=args.log)

if __name__ == "__main__":
    main()