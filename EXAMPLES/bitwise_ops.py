
a = 0b10101010  # a and b are integers
b = 0b11110000

c = a & b  # bitwise AND
print("  {:08b}".format(a))
print("& {:08b}".format(b))
print("  --------")
print("  {:08b}".format(c))
print()

c = a | b # bitwise OR
print("  {:08b}".format(a))
print("| {:08b}".format(b))
print("  --------")
print("  {:08b}".format(c))
print()

c = a ^ b # bitwise XOR
print("  {:08b}".format(a))
print("^ {:08b}".format(b))
print("  --------")
print("  {:08b}".format(c))
print()

c = ~a # complement (flip bit values)
print(" ~ {:09b}".format(a))
print("   {:09b}".format(c))
print()

c = a >> 1 # shift right 1 bit
print("{:08b} >> 1".format(a))
print("{:08b}".format(c))
print()

c = a >> 3 # shift right 3 bits
print("{:08b} >> 3".format(a))
print("{:08b}".format(c))
print()

c = a << 1 # shift left 1 bit
print("{:012b} << 1".format(a))
print("{:012b}".format(c))
print()

c = a << 3 # shift left 3 bits
print("{:012b} << 3".format(a))
print("{:012b}".format(c))
print()
