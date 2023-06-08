import os

def get_file_size(folder, file_name):
    file_path = os.path.join(folder, file_name)
    return os.path.getsize(file_path)

print(f"get_file_size('DATA', 'alice.txt'): {get_file_size('DATA', 'alice.txt')}")
print(f"get_file_size('EXAMPLES', 'zipfile_ex.py'): {get_file_size('EXAMPLES', 'zipfile_ex.py')}")

file_info = ['DATA', 'mary.txt']

print(f"get_file_size(file_info[0], file_info[1]): {get_file_size(file_info[0], file_info[1])}")
print(f"get_file_size(*file_info): {get_file_size(*file_info)}")


file_list = [
    ('DATA', 'presidents.txt'),
    ('ANSWERS', 'fun_with_dates.py'),
    ('DATA', 'wombats.csv'),
]

for file_info in file_list:
    try:
        size = get_file_size(*file_info)
    except FileNotFoundError as err:
        print(err)
    else:
        print(size)
print('-' * 60)

for folder, file_name in file_list:
    try:
        size = get_file_size(folder, file_name)
    except FileNotFoundError as err:
        print(err)
    else:
        print(size)
print('-' * 60)



