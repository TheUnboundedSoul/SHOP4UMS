import sqlite3

# Conectar à base de dados
conn = sqlite3.connect('D:\\Faculdade\\Mestrado\\2 Semestre\\Arquitetura de Software\\SHOP4UMS\Artigo\database\\artigo.db')
cursor = conn.cursor()

# Listar todas as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(tables)  # Verificar se a tabela 'artigo' está na lista

conn.close()
