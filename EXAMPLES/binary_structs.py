
from struct import Struct

values = 7, 6, 42.3, b'Guido' # create some assoted values

demo = Struct('iif10s')  # create Struct object with desired data layout

print("Size of data: {} bytes".format(demo.size)) # size property gives size of data in bytes

binary_stream = demo.pack(*values) # pack() converts values into binary stream using format
#               demo.pack(values[0], values[1], values[2], values[3])

int1, int2, float1, raw_bytes = demo.unpack(binary_stream) # unpack() converts binary stream into list of values
str1 = raw_bytes.decode().rstrip('\x00')  # decode the raw bytes into a string, and strip off trailing null bytes (that were added by pack())

print(raw_bytes)
print(int1, int2, float1, str1)
