import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print("Error: Source directory does not exist.")
        return

    # Check if destination directory exists, create if not
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate through files in source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)

        # If file with same name exists in destination, append timestamp
        while os.path.exists(dest_path):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            base, extension = os.path.splitext(filename)
            filename = f"{base}_{timestamp}{extension}"
            dest_path = os.path.join(dest_dir, filename)

        # Copy file from source to destination
        try:
            shutil.copy2(source_path, dest_path)
            print(f"Copied {source_path} to {dest_path}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Check if correct number of command-line arguments provided
    if len(sys.argv) != 3:
        print("Usage: python file_backup.py /path/to/source /path/to/destination")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    backup_files(source_dir, dest_dir)
