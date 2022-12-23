import sys


def dive_into_python():
        
    # size
    aa = {"a":"b"}  

    # refcount
    print("sys.getrefcount(a):", sys.getrefcount(aa))
    bb = aa
    print("sys.getrefcount(a):", sys.getrefcount(aa))
    cc = aa
    print("sys.getrefcount(a):", sys.getrefcount(aa))

    print(locals())

    aa = 2
    # size
    print("sys.getsizeof(int):", sys.getsizeof(int()))
    print("sys.getsizeof(int):", sys.getsizeof(aa))
    
    # all is object
    print("dir(a):", dir(aa))
    print("a.real:", aa.real)




if __name__ == "__main__":
    # python apps/main/console_scripts.py
    dive_into_python()
