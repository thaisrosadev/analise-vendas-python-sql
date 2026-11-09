import sqlite3                  # traz a ferramenta de banco SQLite, que já vem com o Python
import pandas as pd             # traz o pandas e dá a ele o apelido pd

PASTA_CSV = r"C:\Users\rosat\Downloads\archive"  # onde estão os arquivos baixados (mantenha o r antes das aspas)

conexao = sqlite3.connect("olist.db")  # abre (ou cria) o arquivo do banco, a "despensa"Sua frase está quase certa. A correção: o to_sql cria a tabela e insere os dados de uma vez, e você não escreve o CREATE TABLE nem o INSERT. O pandas gera isso sozinho e descobre o tipo de cada coluna olhando os dados. Com replace, ele apaga a tabela antiga (se existir) e cria de novo.

tabelas = {                                     # um dicionário: nome da prateleira -> arquivo CSV
    "orders": "olist_orders_dataset.csv",       # prateleira dos pedidos
    "customers": "olist_customers_dataset.csv"  # prateleira dos clientes
}

for nome, arquivo in tabelas.items():                           # repete para cada prateleira da lista
    df = pd.read_csv(f"{PASTA_CSV}\\{arquivo}")                 # lê o CSV e guarda a tabela na variável df
    df.to_sql(nome, conexao, if_exists="replace", index=False)  # grava a tabela no banco, trocando se já existir
    print(nome, len(df), "linhas carregadas")                   # avisa quantas linhas entraram

conexao.close()  # fecha o banco, como fechar a porta da despensa
print(df.head())   # mostra as 5 primeiras linhas do df na tela

#Não precisa de USE, porque no SQLite o arquivo é o banco. Quando você conecta, já está dentro dele.