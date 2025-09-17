# lista que armazena os usuários
users = []

# função para cadastrar novo usuário
def cadastrarNovoUsuario():
    id = len(users) + 1
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    users.append({"id": id, "nome": nome,"email": email, "senha": senha})

# def saudarUsuario(user):
#     print(f"Hello, {user}!", "---------------------", sep="\n")

#Lista os usuários cadastrados 
def listarUsuarios(users):
    print("Listas de usuários cadastrados:")
    for user in users:
        print("Usuário ", user["id"],": Nome:", user["nome"],", Email:", user["email"])
    print("-----------------")

#Exclui um usuário pelo id
def excluirUsuario():
    id = int(input("Digite o id do usuário: "))
    for user in users:
        if user["id"] == id:
            users.remove(user)
            print("Usuário removido com sucesso!")

#menu principal
def menu():
    while True:
        print("Seja bem vindo ao nosso sistema! O que deseja realizar?", "1. Cadastrar usuário", "2. Verificar usuários cadastrados", "3. Excluir usuário", "4. Sair", sep="\n")
        opcao = int(input("Digite aqui: "))

        if opcao == 1:
            cadastrarNovoUsuario()
        elif opcao == 2:
            listarUsuarios(users)
        elif opcao == 3:
            excluirUsuario()
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Por favor, digite uma opção válida.")
            
#chama o menu principal
menu()

    