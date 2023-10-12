import sys


def dive_into_python():
    # TODO lesson1
    a = {"key":"value"}  

    # refcount
    print("sys.getrefcount(a):", sys.getrefcount(a))
    b = a
    print("sys.getrefcount(a):", sys.getrefcount(a))
    c = a
    print("sys.getrefcount(a):", sys.getrefcount(a))

    print(locals())

    a = 2
    # size int
    print("sys.getsizeof(int):", sys.getsizeof(int()))
    print("sys.getsizeof(int):", sys.getsizeof(a))
    
    # all is object
    print("dir(a):", dir(a))
    print("a.real:", a.real)



if __name__ == "__main__":
    # python apps/main/console_scripts.py
    dive_into_python()
