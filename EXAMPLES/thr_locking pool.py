from threading import Lock
from multiprocessing.dummy import Pool
import random
import time

WORDS = 'apple banana mango peach papaya cherry lemon watermelon fig elderberry'.split()

MAX_SLEEP_TIME = 3
WORD_LIST = []  # the threads will append words to this list

def make_upper(word):  # function invoked by each thread
    return word.upper()

pool = Pool(4)
results = pool.map(make_upper, WORDS)   # could be  [('a', 1), ('m', 19) ...]

print("Before:", WORDS)
print("After:", results)
