def count_people(people: list)->dict:
    ins = {}
    for persona in personas:
        if not persona in ins:
            ins[persona] = 1
        elif persona in ins:
            ins[persona] += 1
    return  ins

if __name__ == '__main__':
    personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]
    print(count_people(personas))