
def get_message():
    return "Hello ALDOT world"

m = get_message()
print(f"m: {m}")

def say_hello():
    print("Hello hello hello")

say_hello()
x = say_hello()
print(f"x: {x}")

def shout_message(message):
    print(message.upper())

shout_message(m)

shout_message(get_message())

shout_message("45 minutes to lunch!")

def mini_grep(search_term, *file_paths, ignore_case=False):
    lines = []
    if ignore_case:
        search_term = search_term.lower()
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if ignore_case:
                    search_line = raw_line.lower()
                else:
                    search_line = raw_line
                if search_term in search_line:
                    line = raw_line.rstrip()
                    lines.append(line)
    return lines

found_lines = mini_grep('lizard', 'DATA/alice.txt', 'DATA/parrot.txt', 'DATA/words.txt', ignore_case=True)
for line in found_lines:
    print(line)

def config(**kwargs):
    print(kwargs)

config(file_name="wombats.txt", country="Burkina Faso", color="chartreuse")

def wacky(p0, /, p1, p2, *p3, p4, p5, **p6):  # 5 types of parameters
    pass




