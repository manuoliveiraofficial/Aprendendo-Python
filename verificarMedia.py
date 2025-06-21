def main():
    nota1 = float(input("Digite sua nota do primeiro bimestre: "))
    nota2 = float(input("Digite sua nota do segundo bimestre:"))
    nota3 = float(input("Digite sua nota do terceiro bimestre: "))
    nota4 = float(input("Digite sua nota do quarto bimestre: "))
    media = calcularMedia(nota1, nota2, nota3, nota4)
    if  6 <= media <= 10:
        print(f"Sua média é {media}. Aprovado")
    elif media < 6:
        print(f"Sua média é {media}. Reprovado")
    else:
        print("A média está fora da tabela")



def calcularMedia(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    media = round(media, 2)
    return media

main()