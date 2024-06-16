from tabulate import tabulate

# Definindo o banco de dados
banco_dados = {}
proximo_id = 1

# Função para inserir um novo piloto
def insere_piloto(nome, equipe, data_nascimento, local_nascimento, classificacao, vitorias, podios):
    global proximo_id
    banco_dados[proximo_id] = {
        'nome': nome,
        'equipe': equipe,
        'data_nascimento': data_nascimento,
        'local_nascimento': local_nascimento,
        'classificacao': classificacao,
        'vitorias': vitorias,
        'podios': podios
    }
    proximo_id += 1

# Função para atualizar os dados dos pilotos
def atualiza_piloto(id, nome=None, equipe=None, data_nascimento=None, local_nascimento=None, classificacao=None, vitorias=None, podios=None):
    if id in banco_dados:
        if nome is not None:
            banco_dados[id]['nome'] = nome
        if equipe is not None:
            banco_dados[id]['equipe'] = equipe
        if data_nascimento is not None:
            banco_dados[id]['data_nascimento'] = data_nascimento
        if local_nascimento is not None:
            banco_dados[id]['local_nascimento'] = local_nascimento
        if classificacao is not None:
            banco_dados[id]['classificacao'] = classificacao
        if vitorias is not None:
            banco_dados[id]['vitorias'] = vitorias
        if podios is not None:
            banco_dados[id]['podios'] = podios
    else:
        print(f"Piloto com ID {id} não encontrado.")

# Função para excluir um piloto do banco de dados
def exclui_piloto(id):
    if id in banco_dados:
        del banco_dados[id]
    else:
        print(f"Piloto com ID {id} não encontrado.")

# Função para consultar um piloto pelo nome
def consulta_piloto(nome):
    for id, dados in banco_dados.items():
        if dados['nome'] == nome:
            return formatar_dados_piloto(id, dados)
    return f"Piloto {nome} não encontrado."

# Função para formatar os dados do piloto
def formatar_dados_piloto(id, dados):
    return [id, dados['nome'], dados['equipe'], dados['data_nascimento'], dados['local_nascimento'], dados['classificacao'], dados['vitorias'], dados['podios']]

# Função para listar todas as equipes
def listar_equipes():
    equipes = set()
    for dados in banco_dados.values():
        equipes.add(dados['equipe'])
    return equipes

# Função para listar os pilotos de uma equipe específica
def listar_pilotos_por_equipe(equipe):
    pilotos = []
    for id, dados in banco_dados.items():
        if dados['equipe'] == equipe:
            pilotos.append(formatar_dados_piloto(id, dados))
    return pilotos

# Função para exibir o menu de equipes
def menu_equipes():
    equipes = listar_equipes()
    while True:
        print("\nEquipes:")
        for idx, equipe in enumerate(equipes, start=1):
            print(f"{idx}. {equipe}")
        print("0. Voltar")
        opcao = input("Escolha uma equipe para ver mais informações (ou 0 para voltar): ")
        
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 0:
                break
            elif 1 <= opcao <= len(equipes):
                equipe_selecionada = list(equipes)[opcao - 1]
                pilotos = listar_pilotos_por_equipe(equipe_selecionada)
                if pilotos:
                    headers = ["ID", "Nome", "Equipe", "Data de Nascimento", "Local de Nascimento", "Classificação", "Vitórias", "Pódios"]
                    print(tabulate(pilotos, headers=headers, tablefmt="grid"))
                else:
                    print(f"Não há pilotos na equipe {equipe_selecionada}.")
            else:
                print("Opção inválida, tente novamente.")
        else:
            print("Opção inválida, tente novamente.")

# Função para exibir o menu interativo principal
def menu():
    while True:
        print("\nMenu Interativo:")
        print("1. Inserir novo piloto")
        print("2. Atualizar dados de um piloto")
        print("3. Excluir um piloto")
        print("4. Consultar um piloto")
        print("5. Exibir todos os pilotos")
        print("6. Listar equipes")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            equipe = input("Equipe: ")
            data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
            local_nascimento = input("Local de Nascimento: ")
            classificacao = input("Classificação: ")
            vitorias = int(input("Vitórias: "))
            podios = int(input("Pódios: "))
            insere_piloto(nome, equipe, data_nascimento, local_nascimento, classificacao, vitorias, podios)
            print("Piloto inserido com sucesso!")
        
        elif opcao == '2':
            id = int(input("ID do piloto a ser atualizado: "))
            nome = input("Nome (ou deixe em branco para não alterar): ") or None
            equipe = input("Equipe (ou deixe em branco para não alterar): ") or None
            data_nascimento = input("Data de Nascimento (ou deixe em branco para não alterar): ") or None
            local_nascimento = input("Local de Nascimento (ou deixe em branco para não alterar): ") or None
            classificacao = input("Classificação (ou deixe em branco para não alterar): ") or None
            vitorias = input("Vitórias (ou deixe em branco para não alterar): ")
            vitorias = int(vitorias) if vitorias else None
            podios = input("Pódios (ou deixe em branco para não alterar): ")
            podios = int(podios) if podios else None
            atualiza_piloto(id, nome, equipe, data_nascimento, local_nascimento, classificacao, vitorias, podios)
            print("Dados do piloto atualizados com sucesso!")
        
        elif opcao == '3':
            id = int(input("ID do piloto a ser excluído: "))
            exclui_piloto(id)
            print("Piloto excluído com sucesso!")
        
        elif opcao == '4':
            nome = input("Nome do piloto a ser consultado: ")
            piloto = consulta_piloto(nome)
            headers = ["ID", "Nome", "Equipe", "Data de Nascimento", "Local de Nascimento", "Classificação", "Vitórias", "Pódios"]
            if isinstance(piloto, list):  # Se o piloto foi encontrado
                print(tabulate([piloto], headers=headers, tablefmt="grid"))
            else:
                print(piloto)  # Mensagem de erro
        
        elif opcao == '5':
            pilotos = [formatar_dados_piloto(id, dados) for id, dados in banco_dados.items()]
            headers = ["ID", "Nome", "Equipe", "Data de Nascimento", "Local de Nascimento", "Classificação", "Vitórias", "Pódios"]
            print(tabulate(pilotos, headers=headers, tablefmt="grid"))
        
        elif opcao == '6':
            menu_equipes()
        
        elif opcao == '7':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

# Inserir os pilotos iniciais
pilotos = {
    'Lucas di Grassi': {
        'equipe': 'ABT CUPRA Formula E Team',
        'data_nascimento': '11/08/1984',
        'local_nascimento': 'São Paulo, Brasil',
        'classificacao': '24º',
        'vitorias': 0,
        'podios': 0
    },
    'Nico Müller': {
        'equipe': 'ABT CUPRA Formula E Team',
        'data_nascimento': '25/02/1992',
        'local_nascimento': 'Thun, Suíça',
        'classificacao': '16º',
        'vitorias': 0,
        'podios': 0
    },
    'Jake Dennis': {
        'equipe': 'ANDRETTI FORMULA E',
        'data_nascimento': '16/06/1995',
        'local_nascimento': 'Nuneaton, Reino Unido',
        'classificacao': '1º',
        'vitorias': 4,
        'podios': 8
    },
    'Norman Nato': {
        'equipe': 'ANDRETTI FORMULA E',
        'data_nascimento': '08/07/1992',
        'local_nascimento': 'Cannes, França',
        'classificacao': '10º',
        'vitorias': 1,
        'podios': 1
    },
    'Jean-Éric Vergne': {
        'equipe': 'DS Penske',
        'data_nascimento': '25/04/1990',
        'local_nascimento': 'Pontoise, França',
        'classificacao': '5º',
        'vitorias': 1,
        'podios': 4
    },
    'Stoffel Vandoorne': {
        'equipe': 'DS Penske',
        'data_nascimento': '26/03/1992',
        'local_nascimento': 'Kortrijk, Bélgica',
        'classificacao': '11º',
        'vitorias': 0,
        'podios': 1
    },
    'Robin Frijns': {
        'equipe': 'ENVISION RACING',
        'data_nascimento': '07/08/1991',
        'local_nascimento': 'Maastricht, Países Baixos',
        'classificacao': '21º',
        'vitorias': 0,
        'podios': 0
    },
    'Sébastien Buemi': {
        'equipe': 'Envision Racing',
        'data_nascimento': '31/10/1988',
        'local_nascimento': 'Aigle, Suíça',
        'classificacao': '9º',
        'vitorias': 1,
        'podios': 2
    },
    'Dan Ticktum': {
        'equipe': 'ERT FORMULA E TEAM',
        'data_nascimento': '08/06/1999',
        'local_nascimento': 'Londres, Reino Unido',
        'classificacao': '17º',
        'vitorias': 0,
        'podios': 0
    },
    'Sérgio Sette Câmara': {
        'equipe': 'ERT FORMULA E TEAM',
        'data_nascimento': '23/05/1998',
        'local_nascimento': 'Belo Horizonte, Brasil',
        'classificacao': '22º',
        'vitorias': 0,
        'podios': 0
    },
    'Mitch Evans': {
        'equipe': 'Jaguar TCS Racing',
        'data_nascimento': '24/06/1994',
        'local_nascimento': 'Auckland, Nova Zelândia',
        'classificacao': '2º',
        'vitorias': 3,
        'podios': 7
    },
    'Nick Cassidy': {
        'equipe': 'JAGUAR TCS RACING',
        'data_nascimento': '19/08/1994',
        'local_nascimento': 'Auckland, Nova Zelândia',
        'classificacao': '3º',
        'vitorias': 2,
        'podios': 6
    },
    'Edoardo Mortara': {
        'equipe': 'MAHINDRA RACING',
        'data_nascimento': '12/01/1987',
        'local_nascimento': 'Genebra, Suíça',
        'classificacao': '12º',
        'vitorias': 0,
        'podios': 1
    },
    'Nyck de Vries': {
        'equipe': 'MAHINDRA RACING',
        'data_nascimento': '06/02/1995',
        'local_nascimento': 'Sneek, Países Baixos',
        'classificacao': '19º',
        'vitorias': 0,
        'podios': 0
    },
    'Jehan Daruvala': {
        'equipe': 'MASERATI MSG RACING',
        'data_nascimento': '01/10/1998',
        'local_nascimento': 'Mumbai, Índia',
        'classificacao': '23º',
        'vitorias': 0,
        'podios': 0
    },
    'Maximilian Günther': {
        'equipe': 'MASERATI MSG RACING',
        'data_nascimento': '02/07/1997',
        'local_nascimento': 'Oberstdorf, Alemanha',
        'classificacao': '15º',
        'vitorias': 0,
        'podios': 1
    },
    'Jake Hughes': {
        'equipe': 'NEOM McLaren Formula E Team',
        'data_nascimento': '30/05/1994',
        'local_nascimento': 'Birmingham, Reino Unido',
        'classificacao': '13º',
        'vitorias': 0,
        'podios': 2
    },
    'Sam Bird': {
        'equipe': 'NEOM McLaren Formula E Team',
        'data_nascimento': '09/01/1987',
        'local_nascimento': 'Roehampton, Reino Unido',
        'classificacao': '14º',
        'vitorias': 0,
        'podios': 1
    },
    'Oliver Rowland': {
        'equipe': 'Nissan Formula E Team',
        'data_nascimento': '10/08/1992',
        'local_nascimento': 'Sheffield, Reino Unido',
        'classificacao': '20º',
        'vitorias': 0,
        'podios': 0
    },
    'Sacha Fenestraz': {
        'equipe': 'Nissan Formula E Team',
        'data_nascimento': '28/07/1999',
        'local_nascimento': 'Annecy, França',
        'classificacao': '18º',
        'vitorias': 0,
        'podios': 0
    },
    'Pascal Wehrlein': {
        'equipe': 'TAG Heuer Porsche Formula E Team',
        'data_nascimento': '18/10/1994',
        'local_nascimento': 'Sigmaringen, Alemanha',
        'classificacao': '4º',
        'vitorias': 2,
        'podios': 5
    },
    'António Félix da Costa': {
        'equipe': 'TAG Heuer Porsche Formula E Team',
        'data_nascimento': '31/08/1991',
        'local_nascimento': 'Cascais, Portugal',
        'classificacao': '6º',
        'vitorias': 1,
        'podios': 2
    }
}

# Inserir todos os pilotos no banco de dados
for nome, dados in pilotos.items():
    insere_piloto(nome, dados['equipe'], dados['data_nascimento'], dados['local_nascimento'], dados['classificacao'], dados['vitorias'], dados['podios'])

# Executar o menu interativo
menu()
