


# Como Testar:

Necessário Python estar instalado...

1. faça um ```git clone https://github.com/LuiVLoureiro/Code_Test_Centrao``` // **ou** // faça o download do repositório
2. faça no seu terminal um ```pip install -r requirements.txt```
3. por fim, no seu terminal, faça ```python main.py```


# Criação do Banco de Dados por SQLITE3
Simular banco de dados fictício criado para comportar 100 usuários diferentes.
```python
import sqlite3 as sql

# Criar Database com o nome de centrao
conn = sql.connect('centrao.db')
cursor = conn.cursor()

# Criar tabela Usuario
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Usuario (
      ID INTEGER AUTO_INCREMENT PRIMARY KEY,
      NOME VARCHAR(100), CPF TEXT NOT NULL, RG TEXT, GESTOR VARCHAR(200),
      CARTEIRA_DE_TRABALHO TEXT, DATA_DE_NASCIMENTO DATE,
      ESTADO VARCHAR(100), EMAIL VARCHAR(100), NUMERO_SERIE_PESSOAL TEXT,
      TELEFONE TEXT, COLABORADOR VARCHAR(100), CARGO VARCHAR(100), FUNCAO VARCHAR(100),
      FILIAL VARCHAR(100), LOCAIS_DE_TRABALHO VARCHAR(100), CENTRO_DE_CUSTO TEXT,
      CODIGO_EXTERNO VARCHAR (100), PIS TEXT, CODIGO_EXTERNO_DESLIGADO VARCHAR(100),
      EMAIL_CORPORATIVO VARCHAR(100), QR_CODE TEXT, INICIO DATE, TAMANHO_CAMISA VARCHAR(3),
      ESCALA_VIGENTE TEXT,  VIGENCIA DATE, ADMISSAO DATE, FUSO_HORARIO VARCHAR(100), CALENDARIO_VIGENTE DATE,
      ESTRANGEIRO VARCHAR(3), SEXO VARCHAR(15), TEM_FILHOS VARCHAR(3), MOTIVO VARCHAR(150), DEMISSAO DATE, PIN TEXT
      )
    ''')

# Commitar
conn.commit()
 ```
 # Gerar 100 dados Diferentes
Utilizando a biblioteca Faker e a biblioteca Random, podemos criar dados que serão inseridos no banco de dados para simular a finalização.
*OBS:* Note que a biblioteca random, serve apenas para aleatorizar a escolha de listas, pois a bibluoteca *Faker*, não possuí funções necessárias para todos os tipos de dados que deverão ser inseridos.
```python
from faker import Faker
import random

# Importar Faker para a API Brasileira
fake = Faker('pt_BR')

# Definição de Listas para possíveis respostas de cada Usuário
cargos = ['Estágio', 'Junior', 'Pleno', 'Senior']
sexos = ['Homem', 'Mulher']
funcoes = ['Front-End', 'Back-End', 'Banco de Dados']
filiais = ['Manaus', 'Belém', 'São Paulo']
locais_de_trabalho = ['15 de Novembro', '16 de Novembro', 'Batista Campos']
estados = ['Manaus', 'Belém', 'São Paulo']
fuso_horarios = ['America/Sao_Paulo', 'America/Argentina/Buenos_Aires']
estrangeiro_opcao = ['Sim', 'Não']
tamanho_camisa_opcao = ['pp', 'p', 'm', 'g', 'gg']
filhos_opcao = ['Sim', 'Não']
motivos = ['Gosto daqui', 'Recomendação', 'Fui escolhido', 'Linkedin']

# Looping para adicionar 100 usuários diferentes
# Note: random.choice() servirá para variar as respostas fictícias nas listas criadas acima

for i in range(1, 101):
    id = i
    cargo = random.choice(cargos)
    sexo = random.choice(sexos)
    funcao = random.choice(funcoes)
    filial = random.choice(filiais)
    local_de_trabalho = random.choice(locais_de_trabalho)
    estado = random.choice(estados)
    fuso_horario = random.choice(fuso_horarios)
    estrangeiro = random.choice(estrangeiro_opcao)
    tamanho_camisa = random.choice(tamanho_camisa_opcao)
    filhos = random.choice(filhos_opcao)
    motivo = random.choice(motivos)
    centro_de_custo = str(fake.random_number(digits=8))
    gestor = fake.name()
    nome = fake.name()
    cpf = str(fake.random_number(digits=11))
    rg = str(fake.random_number(digits=9))
    carteira_de_trabalho = str(fake.random_number(digits=11))
    data_de_nascimento = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=65).isoformat()
    email_pessoal = fake.email()
    email_corporativo = fake.email()
    telefone = str(fake.random_number(digits=11))
    admissao = fake.date_this_decade(before_today=True, after_today=False).isoformat()
    demissao = fake.date_this_decade(before_today=True, after_today=False).isoformat()
    inicio = fake.date_this_decade(before_today=True, after_today=False).isoformat()
    calendario_vigente = fake.date_this_decade(before_today=True, after_today=False).isoformat()
    pin = str(fake.random_number(digits=10))
    pis = str(fake.random_number(digits=30))
    qr_code = str(fake.random_number(digits=15))
    numero_de_serie = str(fake.random_number(digits=15))
    codigo_externo = str(fake.random_number(digits=15))
    codigo_externo_desligado = str(fake.random_number(digits=15))
    vigencia = fake.date_this_decade(before_today=True, after_today=False).isoformat()
    escala_vigente = str(fake.random_number(digits=8))
    colaborador = nome

    # Atribuir Váriaveis criadas à uma tupla
    values = (
        id, centro_de_custo, gestor, motivo, filhos, tamanho_camisa, sexo, estado, local_de_trabalho, cargo, funcao, filial, nome, cpf, rg,
        carteira_de_trabalho, data_de_nascimento, email_pessoal, email_corporativo, telefone, admissao, demissao, inicio, calendario_vigente,
        pin, pis, qr_code, numero_de_serie, codigo_externo, codigo_externo_desligado, vigencia, fuso_horario, escala_vigente, estrangeiro, colaborador
        )

    # Utilizar Comando para Inserir na Database centro.db e na tabela Usuario
    sql_insert = '''
    INSERT INTO Usuario (
        ID, CENTRO_DE_CUSTO, GESTOR, MOTIVO, TEM_FILHOS, TAMANHO_CAMISA, SEXO, ESTADO, LOCAIS_DE_TRABALHO, CARGO,
        FUNCAO, FILIAL, NOME, CPF, RG, CARTEIRA_DE_TRABALHO, DATA_DE_NASCIMENTO, EMAIL, EMAIL_CORPORATIVO, TELEFONE,
        ADMISSAO, DEMISSAO, INICIO, CALENDARIO_VIGENTE, PIN, PIS, QR_CODE, NUMERO_SERIE_PESSOAL, CODIGO_EXTERNO,
        CODIGO_EXTERNO_DESLIGADO, VIGENCIA, FUSO_HORARIO, ESCALA_VIGENTE, ESTRANGEIRO, COLABORADOR
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    '''


    cursor.execute(sql_insert, values)
```

# Consultar nossa Tabela no Banco de Dados
Utilizando Pandas para executar e ilustrar a consulta da tabela com o comando `SELECT * FROM Usuario` para podermos ilustrar todas as linhas e colunas do código.

```python
import pandas as pd

# Executar consulta para selecionar todos os registros da tabela Usuario
cursor.execute('SELECT * FROM Usuario')

# Obter os nomes das colunas
colunas = [descricao[0] for descricao in cursor.description]
linhas = cursor.fetchall()

# Criar um DataFrame com os dados obtidos
if linhas:
    df = pd.DataFrame(linhas, columns=colunas)
    # Exibir o DataFrame
    display(df)
else:
    print("A tabela está vazia.")
```
