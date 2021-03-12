def maior_primo(num):

    i = 2
    maiorprimo = num
    while (i < num):
        if (maiorprimo == 2) or (maiorprimo == 3) or (maiorprimo == 5) or (maiorprimo == 7) or (maiorprimo == 11):
            i = num + i
        else:
            if (num % i == 0):
                maiorprimo = num
                x = 2
                while (x < maiorprimo):
                    if (maiorprimo % x == 0):
                       maiorprimo = maiorprimo - 1
                       x = 2
                    else:
                       x = x + 1
            i = i + 1
    return maiorprimo
