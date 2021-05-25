def transform(b):
    for i in range(len(b)-1):
        if b[i] == '1':
            b[i] = '0'
            if b[i+1] == '0':
                b[i+1] = '1'
            else:
                b[i+1] = '0'
        elif b[i] == '1':
            b[i] = '0'
            if b[i+1] == '1':
                b[i+1] = '0'
            else:
                b[i+1] = '1'
    return b


print("For face up card use 0 and face down card use 1")
if __name__ == "__main__":
    cards = input("Enter the number of cards: ")
    a = list(cards)
    print(a)
    while a != transform(a.copy()):
        a = transform(a.copy())
    print(a)