import sqlite3 as sql
from faker import Faker
import random
import pandas as pd


conn = sql.connect('centrao.db')
cursor = conn.cursor()
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
conn.commit()

fake = Faker('pt_BR')
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

