Sistema de Gestão de Pilotos de Formula E

Este projeto é um sistema de gerenciamento de pilotos de Formula E, desenvolvido em Python. Ele permite a inserção, atualização, exclusão e consulta de dados de pilotos, além de listar equipes e seus respectivos pilotos. O sistema utiliza a biblioteca `tabulate` para a formatação e exibição de dados em formato tabular, proporcionando uma interface de texto clara e organizada.

*Funcionalidades*

- [Inserir Piloto](#inserir-piloto)
- [Atualizar Piloto](#atualizar-piloto)
- [Excluir Piloto](#excluir-piloto)
- [Consultar Piloto](#consultar-piloto)
- [Exibir Todos os Pilotos](#exibir-todos-os-pilotos)
- [Listar Equipes](#listar-equipes)
- [Listar Pilotos por Equipe](#listar-pilotos-por-equipe)

*Inserir Piloto*

A funcionalidade de inserção permite adicionar um novo piloto ao banco de dados. O usuário deve fornecer informações detalhadas sobre o piloto, incluindo nome, equipe, data de nascimento, local de nascimento, classificação, número de vitórias e número de pódios. Cada piloto recebe um ID exclusivo automaticamente.

*Atualizar Piloto*

Esta função permite ao usuário atualizar as informações de um piloto já existente. É possível modificar qualquer campo, como nome, equipe, data de nascimento, local de nascimento, classificação, número de vitórias e número de pódios. O ID do piloto permanece o mesmo.

*Excluir Piloto*

A exclusão de um piloto remove permanentemente suas informações do banco de dados. O usuário deve fornecer o ID do piloto a ser excluído. Esta operação é irreversível.

*Consultar Piloto*

A consulta de um piloto permite buscar um piloto específico pelo nome. O sistema retorna todos os dados disponíveis sobre o piloto, formatados em uma tabela clara e organizada.

*Exibir Todos os Pilotos*

Esta funcionalidade lista todos os pilotos registrados no banco de dados, exibindo suas informações em uma tabela. É uma maneira rápida de visualizar todos os dados armazenados.

*Listar Equipes*

A listagem de equipes mostra todas as equipes presentes no banco de dados. Esta funcionalidade é útil para visualizar a distribuição de pilotos entre diferentes equipes.

Listar Pilotos por Equipe
Esta função permite listar todos os pilotos pertencentes a uma equipe específica. O usuário seleciona a equipe de interesse e o sistema exibe uma tabela com todos os pilotos dessa equipe.

*Estrutura do Código*



*Banco de Dados*

O banco de dados é implementado como um dicionário Python (`banco_dados`), onde cada entrada é um piloto identificado por um ID exclusivo. O ID é gerado automaticamente e incrementado a cada novo piloto inserido.

*Funções de Manipulação de Dados*

- `insere_piloto(nome, equipe, data_nascimento, local_nascimento, classificacao, vitorias, podios)`: Adiciona um novo piloto ao banco de dados.
- `atualiza_piloto(id, nome=None, equipe=None, data_nascimento=None, local_nascimento=None, classificacao=None, vitorias=None, podios=None)`: Atualiza as informações de um piloto existente. Apenas os campos fornecidos são modificados.
- `exclui_piloto(id)`: Remove um piloto do banco de dados pelo seu ID.
- `consulta_piloto(nome)`: Busca um piloto pelo nome e retorna seus dados.
- `listar_equipes()`: Retorna um conjunto de todas as equipes presentes no banco de dados.
- `listar_pilotos_por_equipe(equipe)`: Retorna uma lista de pilotos que pertencem a uma equipe específica.
- `formatar_dados_piloto(id, dados)`: Formata os dados de um piloto para exibição.

*Menu Interativo*

O sistema inclui um menu interativo que permite ao usuário acessar todas as funcionalidades descritas. Este menu é implementado em duas funções principais:
- `menu_equipes()`: Exibe as equipes e permite listar pilotos por equipe.
- `menu()`: Exibe o menu principal e permite acesso a todas as funcionalidades do sistema.

*Inserção de Dados Iniciais*

O código inclui um conjunto de pilotos iniciais, que são inseridos automaticamente no banco de dados quando o script é executado. Estes dados fornecem uma base de exemplos para começar a utilizar o sistema.

*Como Usar*

*Instalação de Dependências*

Certifique-se de ter o Python instalado. Você precisará da biblioteca `tabulate` para formatação de tabelas. Instale-a usando o seguinte comando:

pip install tabulate

*Execução do Sistema*

Para executar o sistema, basta rodar o script:

python nome_do_arquivo.py

O menu interativo será exibido, permitindo a escolha das opções desejadas.

*Exemplo de Uso*

*Inserir um Novo Piloto*

Para inserir um novo piloto, utilize a função `insere_piloto`:

insere_piloto("Nome do Piloto", "Equipe", "01/01/1990", "Cidade, País", "1º", 5, 10)

Isso adicionará um piloto com os dados fornecidos ao banco de dados.

*Atualizar um Piloto*

Para atualizar as informações de um piloto existente, utilize a função `atualiza_piloto`:

atualiza_piloto(1, nome="Novo Nome")

Isso atualizará o nome do piloto com ID 1 para "Novo Nome".

*Excluir um Piloto*

Para excluir um piloto, utilize a função `exclui_piloto`:

exclui_piloto(1)

Isso removerá o piloto com ID 1 do banco de dados.

*Consultar um Piloto*

Para consultar um piloto pelo nome, utilize a função `consulta_piloto`:


consulta_piloto("Nome do Piloto")

Isso retornará os dados do piloto com o nome especificado.

*Listar Todos os Pilotos*

Para listar todos os pilotos, utilize a função `formatar_dados_piloto` em conjunto com uma lista:

pilotos = [formatar_dados_piloto(id, dados) for id, dados in banco_dados.items()]

Isso retornará uma lista formatada com todos os pilotos.

*Conclusão*

Este sistema de gestão de pilotos de Formula E oferece uma maneira eficiente e estruturada de gerenciar informações de pilotos e equipes. Com funções abrangentes para inserção, atualização, exclusão e consulta, além de uma interface de menu interativo, o sistema é uma ferramenta poderosa para organização e visualização de dados. Ele é ideal para fãs de Formula E, entusiastas de dados esportivos, ou qualquer pessoa interessada em gerenciamento de informações de equipes de corrida.


Ruan Melo: RM 557599
Pedro Josué: RM 554913
Rodrigo Jimenez; RM558148
Mayla Maricato: RM557754
Luciano Henrique Meriato Junior: RM554546
