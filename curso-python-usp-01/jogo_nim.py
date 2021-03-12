def computador_escolhe_jogada(n, m):
    jogadorComputador = 1

    while jogadorComputador != m:
        if (n - jogadorComputador) % (m+1) == 0:
            return jogadorComputador
        else:
            jogadorComputador = jogadorComputador + 1
    return jogadorComputador


def usuario_escolhe_jogada(n, m):
    jogada = False

    while not jogada: 
        jogador = int(input("Quantas peças você vai tirar? "))
        if jogador > m or jogador < 1:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            jogada = True
    return jogador

def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print("**** Rodada", numeroRodada, "****")
        print()
        partida()
        numeroRodada = numeroRodada + 1
    print()
    print("Placar: Você 0 X 3 Computador")


def partida():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    computador = False

    if n % (m+1) == 0:
        print()
        print("Voce começa!")

    else:
        print()
        print("Computador começa!")
        computador = True

    while n > 0:
        if computador:
            jogadorComputador = computador_escolhe_jogada(n, m)
            n = n - jogadorComputador
            if jogadorComputador == 1:
                print()
                print("O computador tirou uma peça")
            else:
                print()
                print("O computador tirou", jogadorComputador, "peças")

            computador = False
        else:
            jogador = usuario_escolhe_jogada(n, m)
            n = n - jogador
            if jogador == 1:
                print()
                print("Você tirou uma peça")
            else:
                print()
                print("Você tirou", jogador, "peças")
            computador = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print("Agora restam,", n, "peças no tabuleiro.")
                print()

    print("Fim do jogo! O computador ganhou!")


print("Bem-vindo ao jogo do NIM! Escolha:")
print()

print("1 - para jogar uma partida isolada")

jogoPartida = int(input("2 - para jogar um campeonato "))

if jogoPartida == 2:
    print()
    print("Voce escolheu um campeonato!")
    print()
    campeonato()
else:
    if jogoPartida == 1:
        print()
        partida()
