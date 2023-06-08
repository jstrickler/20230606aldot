from president import President
import sys

p = President(26)

print(p.first_name, p.last_name, '\n')

print(f"getattr(p, 'first_name'): {getattr(p, 'first_name')}")
# print(f"getattr(p, 'middle_name'): {getattr(p, 'middle_name')}")

#  getattr()  hasattr()  setattr()  delattr()

def doit(writable_object):
    if hasattr(writable_object, "write"):
        writable_object.write("this is a test\n")
    else:
        raise TypeError("object is not writable")

doit(sys.stderr)

with open("junk.txt", "w") as junk_out:
    doit(junk_out)


def make_a_speech(self):
    print("yadda yadda yadda")
    print("four score and whatever")
    print("My fellow Armenians")

setattr(President, 'make_speech', make_a_speech)


p.make_speech()



