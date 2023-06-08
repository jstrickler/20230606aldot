from pprint import pprint

actor = "Chris Hemsworth"
color = "blue"

def spam():
    print("SPAM!!")

g = globals()

pprint(g)

g['animal'] = "wombat"

print(f"animal: {animal}")

print(f"g['color']: {g['color']}")

g['spam']()

g['toast'] = lambda : print("toast toast toast")

toast()
print()

def eggs(milk, honey):
    how = "scrambled"
    size = "xl"
    print("locals:")
    pprint(locals())    

eggs(5, 10)





