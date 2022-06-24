if __name__ == '__main__':
    tex = "Python"
    #esto rompe
    #(1, 2, 3)[111]
    #print(tex[111])
    print(tex[1])
    print(tex[1:3])
    print(tex[-3])
    print("------")
    for n in tex:
        print(n)
    print(len(tex))
    
    nom = "gustavo"
    ap = "ghioldi"
    
    print(nom+" "+ap)
    print(nom*3)
    print("-------------")
    print("\tGustavo\n\tGhioldi")