def main():
    while True:
        print ('Seja bem vindo ao imprimidor de formas.\nQual forma deseja imprimir? ')
        forma = int(input('1. Quadrado\n2. Triângulo\n3. Retângulo\n4. Sair\n'))

        if forma == 4:
            print('Saindo...')
            break

        tamanho = int(input('Qual o tamanho desejado da forma? '))
        imprimirForma(forma, tamanho)
        print('------------------------')

def imprimirForma(forma, tamanho):
    if forma == 1:
        for i in range(tamanho):
            print("*  " * tamanho)

    elif forma == 2:
        for i in range(1, tamanho + 1):
            espacos = " " * (tamanho - i)
            estrelas = "*" * (2 * i - 1)
            print(espacos + estrelas)

    elif forma == 3:
        for i in range(tamanho):
            largura = int(tamanho + (tamanho / 2))
            print("*  " * largura)
            i += 1

    else:
        print ('Opção inválida')
main()