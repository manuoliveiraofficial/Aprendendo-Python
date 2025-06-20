#Calculadora
def main():
    print ('Olá! Bem vindo a calculadora')
    nome = input('Digite seu nome: ')
    print(f'Boas-vindas, {nome}!')

    print(f'Digite: \n1 para somar\n2 para subtrair \n3 para multiplicar \n4 para dividir' )
    opcao = int(input('Digite aqui: '))
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))

    if opcao == 1:
        resultado = somarDoisNumeros(n1, n2)
    elif opcao == 2:
        resultado = subtrairDoisNumeros(n1, n2)
    elif opcao == 2:
        resultado = multiplicarDoisNumeros(n1, n2)
    elif opcao == 2:
        resultado = dividirDoisNumeros(n1, n2)
    else:
        print('Opção inválida')

    print(round(resultado, 2))

def somarDoisNumeros(n1, n2):
    return n1 + n2

def subtrairDoisNumeros(n1, n2):
    return n1 - n2

def multiplicarDoisNumeros(n1, n2):
    return n1 * n2

def dividirDoisNumeros(n1, n2):
    return n1 / n2

main()