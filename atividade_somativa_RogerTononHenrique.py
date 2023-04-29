#Nome: Roger Tonon Henrique
#Cuso: Análise e Desenvolvimento de Sistemas 1º Semestre



#Lista com nome dos estudantes
estudantes = list()
opcao = int
dev = str("\nEm desenvolvimento. \nVolte nas próximas semanas !\n")

while True:
#Menu principal
    print("--- Menu Principal ---")
    print("1) Gerenciar estudantes")
    print("2) Gerenciar professores")
    print("3) Gerenciar disciplinas")
    print("4) Gerenciar turmas")
    print("5) Gerenciar matrículas")
    print("9) Sair \n")
    opcao = int(input("Informe a ação desejada: "))
#Se a opção for 9 retorne uma mensagem e encerre
    if opcao == 9:
        print("\nInteração encerrada. Obrigado !\n")
        break
#Se a opção for diferente de 1 retorne uma mensagem e volte ao menu inicial
    elif opcao != 1:
        print(dev)
#Menu estudantes
#Se a opção for 1 siga para o segundo menu
    elif opcao == 1:
        while True:
            print("--- Estudantes --- Menu de Operações ")
            print("1) Incluir")
            print("2) Listar")
            print("3) Atualizar")
            print("4) Excluir")
            print("9) Voltar ao menu principal \n")
            opcao = int(input("Informe a ação desejada: "))
#Se a opção for 9 encerra a interação com este Menu
            if opcao == 9:
                break
#Se a opção for 1 siga com a inclusão do nome do estudante
            elif opcao == 1:
                print("\n --- Inclusão --- \n")
                nome = input("Informe o nome do estudante: ")
                estudantes.append(nome)
                input("Cadastro efetuado com sucesso.\nPressiona enter para continuar \n ")
#Se a opção for dois, e a lista de estudantes estiver zerada retorne uma mensagem
            elif opcao == 2 and estudantes == []:
                print("\nNão há estudantes cadastrados \n")
#Se não estiver vazia, retorne a lista de estudantes na ordem ascendente
            elif opcao == 2:
                print("\n --- Listagem de estudantes --- \n")
                for nome in estudantes:
                    print(nome)
                input("\nPressiona enter para continuar\n")
#Se a opção for diferente de 1 Incluir ou 2 Listar retorne uma mensagem
            elif opcao != 1 or 2:
                    print(dev)
            else:
                print("\n Em desenvolvimento \n")