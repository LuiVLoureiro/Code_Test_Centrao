# Criação do Banco de Dados por SQLITE3

Simular banco de dados fictício criado para comportar 100 usuários diferentes.

Deve conter os seguintes dados:

 - ID
 - Colaborador (Nome)
 - Cargo
 - Função
 - Filial
 - Locais de Trabalho
 - Centro de Custo
 - Data de Nascimento
 - CPF
 - RG
 - PIS
 - Carteira de Trabalho
 - Nº de Série
 - Email Pessoal
 - Telefone para Contato
 - Estado
 - Código Externo
 - Início
 - Vigência
 - Admissão
 - Fuso Horário
 - Gestor
 - Escala Vigente
 - Calendário Vigente
 - QR Code
 - Estrangeiro
 - Email Corporativo
 - Sexo
 - Tem Filhos
 - Tamanho de Camisa
 - Motivo
 - Demissão
 - PIN


 # Gerar 100 dados Diferentes

Utilizando a biblioteca Faker e a biblioteca Random, podemos criar dados que serão inseridos no banco de dados para simular a finalização.

*OBS:* Note que a biblioteca random, serve apenas para aleatorizar a escolha de listas, pois a bibluoteca *Faker*, não possuí funções necessárias para todos os tipos de dados que deverão ser inseridos.

# Consultar nossa Tabela no Banco de Dados

Utilizando Pandas para executar e ilustrar a consulta da tabela com o comando `SELECT * FROM Usuario` para podermos ilustrar todas as linhas e colunas do código.
