def desenhar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))


def verificar_vencedor(tabuleiro, jogador):

    for linha in tabuleiro:
        if linha == [jogador, jogador, jogador]:
            return True

    for coluna in range(3):
        if tabuleiro[0][coluna] == jogador and tabuleiro[1][coluna] == jogador and tabuleiro[2][coluna] == jogador:
            return True

    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True

    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False


def jogar():
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    jogador = "X"

    while True:
        print("Jogador", jogador)
        linha = int(input("Digite o número da linha (1-3): ")) - 1
        coluna = int(input("Digite o número da coluna (1-3): ")) - 1

        if tabuleiro[linha][coluna] != " ":
            print("Posição já preenchida. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador

        desenhar_tabuleiro(tabuleiro)

        if verificar_vencedor(tabuleiro, jogador):
            print("Jogador", jogador, "venceu!")
            break

        if " " not in tabuleiro[0] and " " not in tabuleiro[1] and " " not in tabuleiro[2]:
            print("Empate!")
            break

        jogador = "O" if jogador == "X" else "X"


jogar()
