# 🚀 Pipeline ETL: Python + PostgreSQL

Este projeto consiste em um pipeline robusto de Extração, Transformação e Carga (ETL) desenvolvido em Python. Ele foi estruturado utilizando o paradigma de Orientação a Objetos (POO) para garantir modularidade e escalabilidade, processando milhares de registros e inserindo-os em um banco de dados relacional.

## 🎯 Objetivo do Projeto
Demonstrar a construção de um fluxo de dados automatizado e defensivo. O script lê uma base de dados bruta (CSV), realiza a higienização e padronização das informações utilizando a biblioteca Pandas, e efetua a carga dos dados processados em um servidor PostgreSQL de forma segura.

## 🛠️ Tecnologias Utilizadas
* **Python 3:** Linguagem principal do projeto.
* **Pandas:** Utilizado para manipulação ágil e limpeza (Transformação) dos dados em memória.
* **SQLAlchemy & psycopg2:** Para mapeamento objeto-relacional (ORM) e comunicação direta com o PostgreSQL.
* **PostgreSQL:** Banco de dados relacional utilizado para o armazenamento final (Carga).
* **python-dotenv:** Para gestão segura de variáveis de ambiente e credenciais.
* **Logging:** Sistema integrado para rastreabilidade de eventos e erros durante a execução.

## ⚙️ Arquitetura e Funcionalidades
1. **Geração de Dados (`gerar_dados.py`):** Script auxiliar que gera uma massa de testes volumosa (ex: 5.000 linhas) com dados inconsistentes propositais.
2. **Extração:** Leitura automatizada e tratamento de exceções (ex: arquivo não encontrado).
3. **Transformação:** Remoção de valores nulos (`NaN`) e padronização de strings (ex: conversão de nomes para maiúsculas).
4. **Carga:** Conexão autenticada ao banco de dados e inserção otimizada utilizando o método `to_sql`.

## 🚀 Como executar este projeto na sua máquina

### 1. Pré-requisitos
Certifique-se de ter o Python e o PostgreSQL instalados na sua máquina.

### 2. Configuração do Ambiente
Clone o repositório e instale as dependências listadas:
```bash
git clone https://github.com/cauanm-dev/ETL.git
cd ETL

pip install -r requirements.txt
