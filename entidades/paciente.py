lista_pacientes = [] 

def cadastrar_paciente():
    while True:
        id = len(lista_pacientes)
        nome = input("Digite o nome do paciente: ")

        try:
            telefone = int(input("Digite o telefone do paciente: "))
            cpf = int(input("Digite o CPF do paciente: "))
            idade = int(input("Digite a idade do paciente: "))
        except ValueError:
            print('Erro: Digite apenas números para Telefone, CPF e Idade')
            continue
            
        endereco = input("Digite o endereço do paciente: ")
        email = input("Digite o email do paciente: ")
        comorbidades = input("Digite as comorbidades do paciente: ")
        remedios = input("Digite os remédios do paciente: ")

        paciente = {
            "id": id,
            "nome": nome,
            "telefone": telefone,
            "cpf": cpf,
            "idade": idade,
            "endereço": endereco,
            "email": email,
            "comorbidades": comorbidades,
            "remédios": remedios
        }

        lista_pacientes.append(paciente)
        
        while True:
            opcao = input("Deseja adicionar outro paciente? (Sim/Não) \n").lower()

            if opcao == 'sim':
                break
            elif opcao == 'não':
                return
            else:
                print('Opção inválida.  Responda com "Sim" ou "Não".')

def listar_paciente():
    print()
    print('=== Pacientes Cadastrados === \n ')

    if not lista_pacientes:
        print('Nenhum paciente cadastrado.\n')
    else:
        for i in lista_pacientes:
            print(f"ID: {i['id']}")
            print(f"Nome: {i['nome']}")
            print(f"Telefone: {i['telefone']}")
            print(f"CPF: {i['cpf']}")
            print(f"Idade: {i['idade']}")
            print(f"Endereço: {i['endereço']}")
            print(f"Email: {i['email']}")
            print(f"Comorbidades: {i['comorbidades']}")
            print(f"Remédios: {i['remédios']}")
            print('--------------------------')

def editar_paciente():
    listar_paciente()
    
    if not lista_pacientes:
        return
    
    try:
        id_editar = int(input("Digite o ID do paciente que deseja editar: "))
    except ValueError:
        print('Insira um ID válido.')
        return
    
    for paciente in lista_pacientes:
        if paciente['id'] == id_editar:
            print(f"Paciente encontrado: {paciente['nome']}")
            
            opcoes = ['nome', 'cpf', 'email', 'telefone', 'endereço', 'comorbidades', 'remédios', 'idade']
            
            while True:
                opcao = input('Informe o que você deseja editar: '
                              '(nome, cpf, telefone, endereço, idade, '
                              'comorbidades, remédios, email)\n').lower()
                
                if opcao in opcoes:
                    if opcao in ['cpf', 'idade', 'telefone']:
                        try:
                            alteracao = int(input(f"Digite o novo {opcao}: "))
                        except ValueError:
                            print(f"O valor para {opcao} deve ser numérico.")
                            continue  
                        
                        paciente[opcao] = alteracao
                    else:
                        alteracao = input(f"Digite o novo {opcao}: ")
                        paciente[opcao] = alteracao
                    
                    print(f"{opcao.capitalize()} atualizado com sucesso!")
                    return  
                else:
                    print('Informe uma opção válida.')
                    continue  
                
    print(f'Paciente com ID {id_editar} não encontrado.')

def excluir_paciente():
    listar_paciente()
    
    if not lista_pacientes:
        return
    
    try:
        id_excluir = int(input('Digite o ID do paciente que deseja excluir: '))
        
        for paciente in lista_pacientes:
            if paciente['id'] == id_excluir:
                lista_pacientes.remove(paciente)
                print(f"Paciente com ID {id_excluir} foi removido.")
                break
        else:
            print(f'Paciente com ID {id_excluir} não encontrado.')
            
    except ValueError:
        print('Insira um ID válido.')
