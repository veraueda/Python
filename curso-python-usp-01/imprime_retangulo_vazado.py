
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

x = 1
while x <= altura:
    y = 1
    while y <= largura:
        if x == 1 or x == altura:
            print("#", end = "")
        else:
            if y == 1 or y == largura:
                print("#", end = "")
            else:
                print(" ", end = "")
        y = y + 1
    print()
    x = x + 1
    
