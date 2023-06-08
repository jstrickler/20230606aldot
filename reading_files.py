with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print()

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()   # read file into a string, with embedded \n

