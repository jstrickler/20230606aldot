
# print out a file 10 bytes at a time
CHUNK_SIZE = 25

with open("../DATA/parrot.txt", "rb") as parrot_in: # Add "b" to "r", "w", or "a" for binary mode
    while True:
        chunk = parrot_in.read(CHUNK_SIZE)  # Use read() to read a specified number of bytes
        if chunk == b"":   # Read returns bytes, not str
            break
        print(chunk) # Use decode() to convert bytes to str
