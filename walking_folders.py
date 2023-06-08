import os

START_DIR = "."
MINIMUM_FILE_SIZE = 1024

def main():
    for folder, subfolders, file_names in os.walk(START_DIR):
        print(folder)
        for file_name in file_names:
            if file_name.endswith('.py'):
                file_path = os.path.join(folder, file_name)
                file_size = os.path.getsize(file_path)
                if file_size > MINIMUM_FILE_SIZE:
                    print(f"    {file_size:6d} {file_name}")


if __name__ == "__main__":
    main()