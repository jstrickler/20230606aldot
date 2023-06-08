from datetime import datetime
from collections import Counter
from functools import wraps

NUM_CALLS = Counter()

def doit(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        now = datetime.now().strftime("%x %X")
        print(now)
        result = func(*args, **kwargs)
        name = func.__name__
        NUM_CALLS[name] += 1
        return result
    
    return wrapper

@doit
def alpha(color):
    print("alligator")
    return "swamp"

@doit
def beta(x, y):
    print("bear")
    return "forest"

# alpha = doit(alpha)
# beta = doit(beta)

r1 = alpha("blue")
r2 = alpha("pink")
r3 = beta(5, 10)
print(r1, r2, r3)

@doit
def gamma():
    print("giraffe")
    return 'veldt'

gamma()
gamma()
gamma()

print(f"NUM_CALLS: {NUM_CALLS}")

for f in alpha, beta, gamma:
    print(f.__name__)
print()


