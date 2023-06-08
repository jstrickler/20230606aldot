

class Normal:

    def do_something(self):
        print("doing something")

n = Normal()
n.do_something()

class Callable:
    def __call__(self):
        print("also doing something")

c = Callable()
c()  #  calling instance calls self.__call__()



