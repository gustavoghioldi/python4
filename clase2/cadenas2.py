if __name__ == '__main__':
    hello = str("         Hola mundo,\nchau Mundo!    ")
    hello = hello.strip().lower()
    
    print(hello.startswith("hola"))
    print(hello.startswith("m"))
    print(hello.endswith("!"))
    print(hello.endswith("mundo"))
    print(hello)
    print(repr(hello))
    
    print(hello.replace("mundo", "world"))
    print( hello.split(","))
    print( hello.split())
    
    print(hello.upper())
    
    print(hello.find("mundo"))
    print(hello.find("coco"))
    print(hello.count("mundo"))