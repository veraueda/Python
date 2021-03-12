
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

x = 1
while x <= altura:
    y = 1
    while y <= largura:
        print("#", end = "")
        y = y + 1
    print()
    x = x + 1
    
