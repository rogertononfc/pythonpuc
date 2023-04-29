#Nome: Roger Tonon Henrique
#Cuso: Análise e Desenvolvimento de Sistemas 1º Semestre



#Lista com nome dos estudantes
estudantes = [{}]
disciplinas = [{}]
turmas = [{}]
professores = [{}]
matriculas = [{}]
opcao = int
dev = str("\nEm desenvolvimento. \nVolte nas próximas semanas !\n")
invalido = str("\nOpção inválida. \nTente novamente.\n")

#Definindo o Menu principal e o laço;
def MENU_CENTRAL (estudantes, professores, disciplinas, turmas):
    while True:
        print("--- Menu Principal ---")
        print("1) Gerenciar estudantes")
        print("2) Gerenciar professores")
        print("3) Gerenciar disciplinas")
        print("4) Gerenciar turmas")
        print("5) Gerenciar matrículas")
        print("9) Sair \n")
        opcao = int(input("Informe a ação desejada: "))
#Se a opção for 9 retorne uma mensagem e encerre;
        if opcao == 9:
            print("\nFinalizando a interação. Obrigado !\n")
            break
        elif opcao == 1:
            MENU_DOS_ALUNOS(estudantes)
        elif opcao == 2:
            MENU_DOS_PROFESSORES(professores)
        elif opcao == 3:
            MENU_DAS_DISCIPLINAS(disciplinas)
        elif opcao == 4:
            MENU_DAS_TURMAS(turmas)
##        elif opcao == 5:
            MENU_DOS_MATRICULAS(matriculas)
        else:
            print("\nPor favor tente novamente com uma opção válida.\n")

#Menu dos estudantes e as validações de acordo com a opção informada;
def MENU_DOS_ALUNOS (estudantes):
    while True:
        print("--- Estudantes --- Menu de Operações ")
        print("1) Incluir")
        print("2) Listar")
        print("3) Atualizar")
        print("4) Excluir")
        print("9) Voltar ao menu principal \n")
        opcao_menuestudante = int(input("\nInforme a ação desejada: \n"))

        if opcao_menuestudante == 9:
            break
        elif opcao_menuestudante == 1:
            ADICIONA_ESTUDANTE(estudantes)
        elif opcao_menuestudante == 2:
            LISTA_ESTUDANTES(estudantes)
        elif opcao_menuestudante == 3:
            ATUALIZA_ESTUDANTE(estudantes)
        elif opcao_menuestudante == 4:
            REMOVER_ESTUDANTE(estudantes)
        else:
            print(invalido)
#Importando uma biblioteca para utilizar a função tempo;
import time

#Criando a opção de adicionar estudantes
def ADICIONA_ESTUDANTE (estudantes):
    print("\n--- Estudantes ---\nIncluir")
    nome_estudante = str(input("Digite o nome do estudante: "))
    cod_estudante = int(input("\nDigite o código para este Estudante: "))
    cpf_estudante = input("\nInforme o CPF do estudante: ")
    input("\nPara continuar, pressiona ENTER")
    print("Salvando as informações, por favor aguarde...")
    time.sleep(2)

#Aqui ele verifica se o código informado já existe, caso exista mostre a mensagem e retorne para validação;
    for estudante in estudantes:
        if estudante["Código"] == cod_estudante:
            print("\nJá existe um cadastro com este código.\n")
            return
    INFO_ESTUDANTE = {"Código":cod_estudante, "Nome":nome_estudante, "CPF":cpf_estudante}
    estudantes.append(INFO_ESTUDANTE)
    ESTUDANTE_ARQUIVO(estudantes)
    print("\nCadastro finalizado com sucesso !\n")

def LISTA_ESTUDANTES (estudantes):
    print("\nCarregando dados, por favor aguarde.\n")
    time.sleep(3)
    if len(estudantes) ==0:
        print("\n\n\nNenhum cadastro encontrado.\n")
    else:
        print("--- Lista de estudantes ---")
        for estudante in estudantes:
            print(estudante)
        input("\nPressiona enter para continuar\n")
def ATUALIZA_ESTUDANTE (estudantes):
    print("--- Atualizar estudantes ---")
    codigo = int(input("\nQual código do estudante que quer atualizar ?\n"))
    for estudante in estudantes:
        if estudante["Código"] == codigo:
            nome_estudante = input("\nQual o novo nome do estudante: \n")
            cpf_estudante = input("\nInforme o CPF do estudante: \n")
            if nome_estudante and cpf_estudante:
                atualiza_codigo = int(input("\nQual o novo código do estudante ?\n"))
                print("\nCarregando dados, por favor aguarde.\n")
                time.sleep(3)
                for diferente_estudante in estudantes:
                    if diferente_estudante["Código"] == atualiza_codigo and diferente_estudante != estudante:
                        print("\nJá existe um cadastro com este código.\n")
                        return
                estudante["Nome"] = nome_estudante
                estudante['CPF'] = cpf_estudante
                estudante['Código'] = atualiza_codigo
                print("Aluno com código {} atualizado com sucesso".format(codigo))
                ESTUDANTE_ARQUIVO(estudantes)
                break
            else:
                print("Algum campo não foi preenchido, por favor revise")
                return
    else:
        print("Aluno com código {} não foi encontrado".format(codigo))

def REMOVER_ESTUDANTE (estudantes):
    print("\n --- Excluir --- \n")
    codigo = int(input("\nQual o código que deseja remover ? \n"))
    for estudante in estudantes:
        if estudante["Código"] == codigo:
            estudantes.remove(estudante)
            input("\nPara remover o aluno {}, aperte ENTER\n".format(estudante))
            print("\nExclusão em andamento, aguarde\n")
            time.sleep(3)
            print("\nRemoção realizada com sucesso para o aluno código{}.\n".format(codigo))
            ESTUDANTE_ARQUIVO(estudantes)
            break
    else:
        print("\nEstudante com código {}, não foi encontrado\n".format(codigo))

#Importando biblioteca para usar o json
import json

#Definindo a função para salvar o arquivo de estudantes;
def ESTUDANTE_ARQUIVO(estudantes):
    with open ("estudantes.json", "w") as file:
        json.dump(estudantes, file)
        file.close()
    print("\n\nA lista foi salva !\n\n")
import json

#Definindo o arquivo que será importado os novos estudantes;
def UPLOAD_ESTUDANTES():
    try:
        with open ("estudantes.json", "r") as file:
           estudantes = json.load(file)
           file.close()
    except FileNotFoundError:
        estudantes = []
    return estudantes
import json

#Gravando os dados na lista;
def GRAVA_ESTUDANTES (estudantes):
    with open("estudantes.json","r") as file:
        json.dump(estudantes, file)
        file.close()
#Para importar os dados dos estudantes;
def CARREGA_ESTUDANTES (estudantes):
    try:
        with open("estudantes.json","r") as file:
            estudantes = json.load(file)
            file.close()
    except FileNotFoundError:
        estudantes = []
    return estudantes

#Segundo menu de Professores


#Menu dos professores e as validações de acordo com a opção informada;
def MENU_DOS_PROFESSORES (professores):
    while True:
        print("--- Professores --- Menu de Operações ")
        print("1) Incluir")
        print("2) Listar")
        print("3) Atualizar")
        print("4) Excluir")
        print("9) Voltar ao menu principal \n")
        opcao_menuprofessor = int(input("\nInforme a ação desejada: \n"))

        if opcao_menuprofessor == 9:
            break
        elif opcao_menuprofessor == 1:
            ADICIONA_PROFESSOR(professores)
        elif opcao_menuprofessor == 2:
            LISTA_PROFESSOR(professores)
        elif opcao_menuprofessor == 3:
            ATUALIZA_PROFESSOR(professores)
        elif opcao_menuprofessor == 4:
            REMOVER_PROFESSOR(professores)
        else:
            print(invalido)
#Importando uma biblioteca para utilizar a função tempo;
import time

#Criando a opção de adicionar professores
def ADICIONA_PROFESSOR (professores):
    print("\n--- Professores ---\nIncluir")
    nome_professor = str(input("Digite o nome do professor: "))
    cod_professor = int(input("\nDigite o código para este professor: "))
    cpf_professor = input("\nInforme o CPF do professor: ")
    input("\nPara continuar, pressiona ENTER")
    print("Salvando as informações, por favor aguarde...")
    time.sleep(2)

#Aqui ele verifica se o código informado já existe, caso exista mostre a mensagem e retorne para validação;
    for professor in professores:
        if professor["Código"] == cod_professor:
            print("\nJá existe um cadastro com este código.\n")
            return
    INFO_PROFESSOR = {"Código":cod_professor, "Nome":nome_professor, "CPF":cpf_professor}
    professores.append(INFO_PROFESSOR)
    PROFESSOR_ARQUIVO(professores)
    print("\nCadastro finalizado com sucesso !\n")

def LISTA_PROFESSOR (professores):
    print("\nCarregando dados, por favor aguarde.\n")
    time.sleep(3)
    if len(professores) ==0:
        print("\n\n\nNenhum cadastro encontrado.\n")
    else:
        print("--- Lista de professores ---")
        for professor in professores:
            print(professor)
        input("\nPressiona enter para continuar\n")
def ATUALIZA_PROFESSOR (professores):
    print("--- Atualizar professores ---")
    codigo = int(input("\nQual código do professor que quer atualizar ?\n"))
    for professor in professores:
        if professor["Código"] == codigo:
            nome_professor = input("\nQual o novo nome do professor: \n")
            cpf_professor = input("\nInforme o CPF do professor: \n")
            if nome_professor and cpf_professor:
                atualiza_codigo = int(input("\nQual o novo código do professor ?\n"))
                print("\nCarregando dados, por favor aguarde.\n")
                time.sleep(3)
                for diferente_professor in professores:
                    if diferente_professor["Código"] == atualiza_codigo and diferente_professor != professor:
                        print("\nJá existe um cadastro com este código.\n")
                        return
                professor["Nome"] = nome_professor
                professor['CPF'] = cpf_professor
                professor['Código'] = atualiza_codigo
                print("Aluno com código {} atualizado com sucesso".format(codigo))
                PROFESSOR_ARQUIVO(professores)
                break
            else:
                print("Algum campo não foi preenchido, por favor revise")
                return
    else:
        print("Aluno com código {} não foi encontrado".format(codigo))

def REMOVER_PROFESSOR (professores):
    print("\n --- Excluir --- \n")
    codigo = int(input("\nQual o código que deseja remover ? \n"))
    for professor in professores:
        if professor["Código"] == codigo:
            professores.remove(professor)
            input("\nPara remover o aluno {}, aperte ENTER\n".format(professor))
            print("\nExclusão em andamento, aguarde\n")
            time.sleep(3)
            print("\nRemoção realizada com sucesso para o aluno código{}.\n".format(codigo))
            PROFESSOR_ARQUIVO(professores)
            break
    else:
        print("\nProfessor com código {}, não foi encontrado\n".format(codigo))

#Importando biblioteca para usar o json
import json

#Definindo a função para salvar o arquivo de professores;
def PROFESSOR_ARQUIVO(professores):
    with open ("professores.json", "w") as file:
        json.dump(professores, file)
        file.close()
    print("\n\nA lista foi salva !\n\n")
import json

#Definindo o arquivo que será importado os novos professores;
def UPLOAD_PROFESSOR():
    try:
        with open ("professores.json", "r") as file:
           professores = json.load(file)
           file.close()
    except FileNotFoundError:
        professores = []
    return professores
import json

#Gravando os dados na lista;
def GRAVA_PROFESSORES (professores):
    with open("professores.json","r") as file:
        json.dump(professores, file)
        file.close()
#Para importar os dados dos estudantes;
def CARREGA_PROFESSORES (professores):
    try:
        with open("professores.json","r") as file:
            professores = json.load(file)
            file.close()
    except FileNotFoundError:
        professores = []
    return professores

#Terceiro menu de disciplinas


#Menu dos disciplinas e as validações de acordo com a opção informada;
def MENU_DAS_DISCIPLINAS (disciplinas):
    while True:
        print("--- disciplinas --- Menu de Operações ")
        print("1) Incluir")
        print("2) Listar")
        print("3) Atualizar")
        print("4) Excluir")
        print("9) Voltar ao menu principal \n")
        opcao_menudisciplina = int(input("\nInforme a ação desejada: \n"))

        if opcao_menudisciplina == 9:
            break
        elif opcao_menudisciplina == 1:
            ADICIONA_DISCIPLINA(disciplinas)
        elif opcao_menudisciplina == 2:
            LISTA_DISCIPLINA(disciplinas)
        elif opcao_menudisciplina == 3:
            ATUALIZA_DISCIPLINA(disciplinas)
        elif opcao_menudisciplina == 4:
            REMOVER_DISCIPLINA(disciplinas)
        else:
            print(invalido)
#Importando uma biblioteca para utilizar a função tempo;
import time

#Criando a opção de adicionar disciplinas
def ADICIONA_DISCIPLINA (disciplinas):
    print("\n--- disciplinas ---\nIncluir")
    nome_disciplina = str(input("Digite o nome do disciplina: "))
    cod_disciplina = int(input("\nDigite o código para este disciplina: "))
    cpf_disciplina = input("\nInforme o CPF do disciplina: ")
    input("\nPara continuar, pressiona ENTER")
    print("Salvando as informações, por favor aguarde...")
    time.sleep(2)

#Aqui ele verifica se o código informado já existe, caso exista mostre a mensagem e retorne para validação;
    for disciplina in disciplinas:
        if disciplina["Código"] == cod_disciplina:
            print("\nJá existe um cadastro com este código.\n")
            return
    INFO_DISCIPLINA = {"Código":cod_disciplina, "Nome":nome_disciplina, "CPF":cpf_disciplina}
    disciplinas.append(INFO_DISCIPLINA)
    DISCIPLINA_ARQUIVO(disciplinas)
    print("\nCadastro finalizado com sucesso !\n")

def LISTA_DISCIPLINA (disciplinas):
    print("\nCarregando dados, por favor aguarde.\n")
    time.sleep(3)
    if len(disciplinas) ==0:
        print("\n\n\nNenhum cadastro encontrado.\n")
    else:
        print("--- Lista de disciplinas ---")
        for disciplina in disciplinas:
            print(disciplina)
        input("\nPressiona enter para continuar\n")
def ATUALIZA_DISCIPLINA (disciplinas):
    print("--- Atualizar disciplinas ---")
    codigo = int(input("\nQual código do disciplina que quer atualizar ?\n"))
    for disciplina in disciplinas:
        if disciplina["Código"] == codigo:
            nome_disciplina = input("\nQual o novo nome do disciplina: \n")
            cpf_disciplina = input("\nInforme o CPF do disciplina: \n")
            if nome_disciplina and cpf_disciplina:
                atualiza_codigo = int(input("\nQual o novo código do disciplina ?\n"))
                print("\nCarregando dados, por favor aguarde.\n")
                time.sleep(3)
                for diferente_disciplina in disciplinas:
                    if diferente_disciplina["Código"] == atualiza_codigo and diferente_disciplina != disciplina:
                        print("\nJá existe um cadastro com este código.\n")
                        return
                disciplina["Nome"] = nome_disciplina
                disciplina['CPF'] = cpf_disciplina
                disciplina['Código'] = atualiza_codigo
                print("Aluno com código {} atualizado com sucesso".format(codigo))
                DISCIPLINA_ARQUIVO(disciplinas)
                break
            else:
                print("Algum campo não foi preenchido, por favor revise")
                return
    else:
        print("Aluno com código {} não foi encontrado".format(codigo))

def REMOVER_DISCIPLINA (disciplinas):
    print("\n --- Excluir --- \n")
    codigo = int(input("\nQual o código que deseja remover ? \n"))
    for disciplina in disciplinas:
        if disciplina["Código"] == codigo:
            disciplinas.remove(disciplina)
            input("\nPara remover o aluno {}, aperte ENTER\n".format(disciplina))
            print("\nExclusão em andamento, aguarde\n")
            time.sleep(3)
            print("\nRemoção realizada com sucesso para o aluno código{}.\n".format(codigo))
            DISCIPLINA_ARQUIVO(disciplinas)
            break
    else:
        print("\nProfessor com código {}, não foi encontrado\n".format(codigo))

#Importando biblioteca para usar o json
import json

#Definindo a função para salvar o arquivo de disciplinas;
def DISCIPLINA_ARQUIVO(disciplinas):
    with open ("disciplinas.json", "w") as file:
        json.dump(disciplinas, file)
        file.close()
    print("\n\nA lista foi salva !\n\n")
import json

#Definindo o arquivo que será importado os novos disciplinas;
def UPLOAD_DISCIPLINA():
    try:
        with open ("disciplinas.json", "r") as file:
           disciplinas = json.load(file)
           file.close()
    except FileNotFoundError:
        disciplinas = []
    return disciplinas
import json

#Gravando os dados na lista;
def GRAVA_DISCIPLINAS (disciplinas):
    with open("disciplinas.json","r") as file:
        json.dump(disciplinas, file)
        file.close()
#Para importar os dados dos estudantes;
def CARREGA_DISCIPLINAS (disciplinas):
    try:
        with open("disciplinas.json","r") as file:
            disciplinas = json.load(file)
            file.close()
    except FileNotFoundError:
        disciplinas = []
    return disciplinas

#Quarto menu de turmas


#Menu dos turmas e as validações de acordo com a opção informada;
def MENU_DAS_TURMAS (turmas):
    while True:
        print("--- turmas --- Menu de Operações ")
        print("1) Incluir")
        print("2) Listar")
        print("3) Atualizar")
        print("4) Excluir")
        print("9) Voltar ao menu principal \n")
        opcao_menuturmas = int(input("\nInforme a ação desejada: \n"))

        if opcao_menuturmas == 9:
            break
        elif opcao_menuturmas == 1:
            ADICIONA_TURMAS(turmas)
        elif opcao_menuturmas == 2:
            LISTA_TURMAS(turmas)
        elif opcao_menuturmas == 3:
            ATUALIZA_TURMAS(turmas)
        elif opcao_menuturmas == 4:
            REMOVER_TURMAS(turmas)
        else:
            print(invalido)
#Importando uma biblioteca para utilizar a função tempo;
import time

#Criando a opção de adicionar turmas
def ADICIONA_TURMAS (turmas):
    print("\n--- turmas ---\nIncluir")
    nome_turmas = str(input("Digite o nome do disciplina: "))
    cod_turmas = int(input("\nDigite o código para este disciplina: "))
    cpf_turmas = input("\nInforme o CPF do disciplina: ")
    input("\nPara continuar, pressiona ENTER")
    print("Salvando as informações, por favor aguarde...")
    time.sleep(2)

#Aqui ele verifica se o código informado já existe, caso exista mostre a mensagem e retorne para validação;
    for disciplina in turmas:
        if disciplina["Código"] == cod_turmas:
            print("\nJá existe um cadastro com este código.\n")
            return
    INFO_TURMAS = {"Código":cod_turmas, "Nome":nome_turmas, "CPF":cpf_turmas}
    turmas.append(INFO_TURMAS)
    DISCIPLINA_ARQUIVO(turmas)
    print("\nCadastro finalizado com sucesso !\n")

def LISTA_TURMAS (turmas):
    print("\nCarregando dados, por favor aguarde.\n")
    time.sleep(3)
    if len(turmas) ==0:
        print("\n\n\nNenhum cadastro encontrado.\n")
    else:
        print("--- Lista de turmas ---")
        for disciplina in turmas:
            print(disciplina)
        input("\nPressiona enter para continuar\n")
def ATUALIZA_TURMAS (turmas):
    print("--- Atualizar turmas ---")
    codigo = int(input("\nQual código do turma que quer atualizar ?\n"))
    for disciplina in turmas:
        if disciplina["Código"] == codigo:
            nome_turmas = input("\nQual o novo nome do disciplina: \n")
            cpf_turmas = input("\nInforme o CPF do disciplina: \n")
            if nome_turmas and cpf_turmas:
                atualiza_codigo = int(input("\nQual o novo código do disciplina ?\n"))
                print("\nCarregando dados, por favor aguarde.\n")
                time.sleep(3)
                for diferente_turmas in turmas:
                    if diferente_turmas["Código"] == atualiza_codigo and diferente_turmas != disciplina:
                        print("\nJá existe um cadastro com este código.\n")
                        return
                disciplina["Nome"] = nome_turmas
                disciplina['CPF'] = cpf_turmas
                disciplina['Código'] = atualiza_codigo
                print("Aluno com código {} atualizado com sucesso".format(codigo))
                DISCIPLINA_ARQUIVO(turmas)
                break
            else:
                print("Algum campo não foi preenchido, por favor revise")
                return
    else:
        print("Turma com código {} não foi encontrado".format(codigo))

def REMOVER_TURMAS (turmas):
    print("\n --- Excluir --- \n")
    codigo = int(input("\nQual o código que deseja remover ? \n"))
    for disciplina in turmas:
        if disciplina["Código"] == codigo:
            turmas.remove(disciplina)
            input("\nPara remover a turma {}, aperte ENTER\n".format(disciplina))
            print("\nExclusão em andamento, aguarde\n")
            time.sleep(3)
            print("\nRemoção realizada com sucesso para a turma código{}.\n".format(codigo))
            DISCIPLINA_ARQUIVO(turmas)
            break
    else:
        print("\nProfessor com código {}, não foi encontrado\n".format(codigo))

#Importando biblioteca para usar o json
import json

#Definindo a função para salvar o arquivo de turmas;
def DISCIPLINA_ARQUIVO(turmas):
    with open ("turmas.json", "w") as file:
        json.dump(turmas, file)
        file.close()
    print("\n\nA lista foi salva !\n\n")
import json

#Definindo o arquivo que será importado os novos turmas;
def UPLOAD_TURMAS():
    try:
        with open ("turmas.json", "r") as file:
           turmas = json.load(file)
           file.close()
    except FileNotFoundError:
        turmas = []
    return turmas
import json

#Gravando os dados na lista;
def GRAVA_TURMAS (turmas):
    with open("turmas.json","r") as file:
        json.dump(turmas, file)
        file.close()
#Para importar os dados dos estudantes;
def CARREGA_TURMAS (turmas):
    try:
        with open("turmas.json","r") as file:
            turmas = json.load(file)
            file.close()
    except FileNotFoundError:
        turmas = []
    return turmas


estudantes = CARREGA_ESTUDANTES(estudantes)
MENU_CENTRAL(estudantes, professores, disciplinas, turmas)
professores = CARREGA_PROFESSORES(professores)
disciplinas = CARREGA_DISCIPLINAS(disciplinas)
turmas = CARREGA_TURMAS(turmas)