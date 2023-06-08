import os

original_folder = os.getcwd()

home_folder = os.getenv('USERPROFILE')
print(f"home_folder: {home_folder}")
os.chdir(home_folder)

current_folder = os.getcwd()
print(f"current_folder: {current_folder}")

os.chdir(original_folder)
print(f"os.getcwd(): {os.getcwd()}")

user_name = os.getenv('USERNAME')
print(f"I am {user_name} and I live at {home_folder}")
