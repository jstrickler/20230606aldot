import os
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"

def main():
    file_path = os.path.join(FOLDER, FILE_NAME)
    print(f"file_path: {file_path}")
    print(f"os.path.abspath(file_path): {os.path.abspath(file_path)}")
    print(f"os.path.dirname(file_path): {os.path.dirname(file_path)}")
    print(f"os.path.basename(file_path): {os.path.basename(file_path)}")
    print(f"os.path.splitext(file_path): {os.path.splitext(file_path)}")
    print(f"os.path.splitdrive(file_path): {os.path.splitdrive(file_path)}")
    abs_path = os.path.abspath(file_path)
    print(f"os.path.splitdrive(abs_path): {os.path.splitdrive(abs_path)}")
    
    file_size = os.path.getsize(file_path)
    print(f"file_size: {file_size}")
    raw_timestamp = os.path.getmtime(file_path)
    print(f"raw_timestamp: {raw_timestamp}")
    file_mod_time = datetime.fromtimestamp(raw_timestamp)
    print(f"file_mod_time: {file_mod_time}")
    
    for path in file_path, 'wombats.txt', 'DATA/mystery':
        print(path, os.path.exists(path), os.path.isfile(path), os.path.isdir(path))
    print()

    # listing contents of folders
    data_files = os.listdir('DATA')
    print(f"data_files: {data_files}")
    print()

    for entry in os.scandir('DATA'):
        print(entry.name, entry.is_dir(), entry.path, entry.stat())
    
    








    
    

if __name__ == "__main__":
    main()