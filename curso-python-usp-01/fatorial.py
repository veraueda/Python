n = int(input("Digite o valor de n: "))
i = 1
auxiliar = n
fatorial = n
if n != 0:
    while (i < n):
        fatorial = fatorial * (auxiliar - 1)
        i = i + 1
        auxiliar = auxiliar - 1
else:
    fatorial = 1
print(fatorial)