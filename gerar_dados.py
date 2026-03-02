import csv
import random
import os

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

PASTA_DATA = os.path.join(DIRETORIO_ATUAL, 'data')

os.makedirs(PASTA_DATA, exist_ok=True)

CAMINHO_ARQUIVO = os.path.join(PASTA_DATA, 'dados_volumosos.csv')

print(f"O arquivo será criado EXATAMENTE aqui: {CAMINHO_ARQUIVO}")

nomes = ['joao silva', 'MARIA SOUZA', 'carlos eduardo', 'ana paula', 'fernando costa', 'JULIANA ALVES', 'roberto carlos', '']
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', '']

with open(CAMINHO_ARQUIVO, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['id', 'nome_cliente', 'idade', 'cidade'])
    
    for i in range(1, 5001):
        nome = random.choice(nomes)
        idade = random.randint(18, 90) if random.random() > 0.1 else '' 
        cidade = random.choice(cidades)
        escritor.writerow([i, nome, idade, cidade])

print("Sucesso! Arquivo gerado.")