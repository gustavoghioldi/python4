class UnAuthorizeError(Exception):
    pass

def usuario(user:str, passw:str):
    if user == "gus" and passw == "123":
        return True
    else:
        raise UnAuthorizeError("usuario no autorizado")

if __name__ == '__main__':
    print("--- inicio programa---")
    try:
        usuario("gus", "123")
    except UnAuthorizeError:
        print("Usuario no autorizado")
    except Exception:
        print("rompio todo")
    usuario("gus", "123222")
    print("-- fin del programa ---")