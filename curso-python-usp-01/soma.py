
tamanho = int(input("Digite o tamanho da sequencia de numeros: "))
soma = 0
i = 0

while i < tamanho:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor
    i = i + 1
print("A soma dos valores digitados é: ", soma)