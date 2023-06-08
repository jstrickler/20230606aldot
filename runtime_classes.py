g = globals()

class Cat:
    def speak(self):
        print("meow!")

c = Cat()
c.speak()
print()

animals = [('Dog', 'woof'), ('Bird', 'tweet'), ('Lion', 'roar')]

def make_method(sound):
    def speak(self):
        print(sound)
    return speak

for animal_name, animal_sound in animals:
    g[animal_name] = type(animal_name, (), {'speak': make_method(animal_sound)})

d = Dog()
b = Bird()
leo = Lion()

d.speak()
b.speak()
leo.speak()

Thing = type('Thing', (), {'spam': lambda self: print('spam')})

t = Thing()
t.spam()