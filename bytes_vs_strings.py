
#  \uXXXX   \UXXXXXXXX

message = "82\u00B0 in Durham"

print(message)
print(f"len(message): {len(message)}")

#  encode using UTF-8
bmessage = message.encode() 
print(f"len(bmessage): {len(bmessage)}")
print(type(message), type(bmessage))

print(f"bmessage: {bmessage}")


m2 = bmessage.decode()
print(m2)




