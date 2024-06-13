import os

# Define o caminho completo para o ficheiro da base de dados
file_path = os.path.abspath(os.path.join(os.getcwd(), '/database', 'artigo.db'))

# Verifica se o diretório existe, caso contrário, cria-o
directory = os.path.dirname(file_path)
if not os.path.exists(directory):
    os.makedirs(directory)

# Agora pode usar o file_path com a certeza de que o diretório existe
print(file_path)  # Apenas para verificar o caminho gerado

# O resto do seu código que utiliza o file_path
