
city = "Montgomery"  # global variable

def spam():
    color = "orange"  # local variable
    city = "Birmingham"
    print(f"city: {city}")
    
spam()

print(f"city: {city}")

