import os
import glob
from pathlib import Path

def clean_tex_files(root_dir='.'):
    """
    Clean up LaTeX auxiliary files (.aux, .log, .out) from all directories
    starting from the given root directory.
    
    Args:
        root_dir (str): The root directory to start cleaning from
    """
    # Convert to Path object for better path handling
    root_path = Path(root_dir)
    
    # File extensions to delete
    extensions = ['.aux', '.log', '.out', '.synctex.gz']
    
    # Counter for deleted files
    deleted_files = 0
    
    # Walk through all directories
    for dirpath, dirnames, filenames in os.walk(root_path):
        for ext in extensions:
            # Find all files with the current extension
            files_to_delete = glob.glob(os.path.join(dirpath, f'*{ext}'))
            
            # Delete each file
            for file_path in files_to_delete:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    deleted_files += 1
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
    
    print(f"\nTotal files deleted: {deleted_files}")

if __name__ == "__main__":
    # Use the current directory as root
    clean_tex_files() 