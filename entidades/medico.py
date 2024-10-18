lista_medicos = []

def cadastrar_medico():    
    while True:
        id = len(lista_medicos)
        nome = input("Digite o nome do médico: ")
        especialidade = input("Digite a especialidade do médico: ")
        email = input("Digite o email do médico: ")
        
        while True:
            try:
                crm = input("Digite o CRM do médico: ")
                telefone = int(input("Digite o telefone do médico: "))
                break
            except ValueError:
                print("Erro: Digite apenas números para o CRM e telefone.")

        print(f"{nome} cadastrado com sucesso")
    
        medico = {
            "id": id,
            "nome": nome,
            "especialidade": especialidade,
            "email": email,
            "crm": crm,
            "telefone": telefone
        }
    
        lista_medicos.append(medico)

        while True:
            opcao = input("Deseja adicionar outro médico? (Sim/Não) \n").lower()

            if opcao == 'sim':
                break
            elif opcao == 'não':
                return
            else:
                print('Opção inválida.  Responda com "Sim" ou "Não".')


def listar_medico():
    print()
    print("Médicos cadastrados: ")
    
    if not lista_medicos:
        print("Nenhum médico cadastrado.")
    else:
        for i in lista_medicos:
            print(f'ID: {i["id"]}') 
            print(f'Nome: {i["nome"]}') 
            print(f'Especialidade: {i["especialidade"]}') 
            print(f'Email: {i["email"]}')
            print(f'CRM: {i["crm"]}') 
            print(f'Telefone: {i["telefone"]}') 
            print()


def editar_medico():
    listar_medico()
    
    if not lista_medicos:
        return
    
    try:
        id_editar = int(input("Digite o ID do médico que deseja editar: "))
    except ValueError:
        print('Insira um ID válido.')
        return
    
    for medico in lista_medicos:
        if medico['id'] == id_editar:
            print(f'Médico encontrado ID: {medico["id"]}, Nome: {medico["nome"]}')

            opcoes = ['nome', 'especialidade', 'email', 'crm', 'telefone']

            while True:
                opcao = input('Informe o que você deseja editar: '
                              '(nome, especialidade, email, crm, telefone)\n').lower()

                if opcao in opcoes:
                    if opcao == 'telefone':
                        try:
                            alteracao = int(input(f"Digite o novo {opcao}: "))
                        except ValueError:
                            print(f"O valor para {opcao} deve ser numérico.")
                            continue
                        medico[opcao] = alteracao
                    else:
                        alteracao = input(f"Digite o novo {opcao}: ")
                        medico[opcao] = alteracao
                        
                    print(f"{opcao.capitalize()} atualizado com sucesso!")
                    return 
                else:
                    print('Informe uma opção válida.')
                    continue 
                
    print(f'Médico com ID {id_editar} não encontrado.')


def excluir_medico():
    listar_medico()
    
    if not lista_medicos:
        return
    
    try:
        id_excluir = int(input('Digite o ID do médico que deseja excluir: '))

        for medico in lista_medicos:
            if medico['id'] == id_excluir:
                lista_medicos.remove(medico)
                print(f'Médico com ID: {id_excluir} foi removido.')
                break
        else:
            print(f'Médico com ID: {id_excluir} não encontrado')
            
    except ValueError:
        print('Digite um número válido para ID')




