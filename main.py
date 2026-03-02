import pandas as pd
from sqlalchemy import create_engine
import logging
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class PipelineETL:
    def __init__(self, caminho_csv: str, string_conexao: str):
        self.caminho_csv = caminho_csv
        self.engine = create_engine(string_conexao)

    def extrair(self) -> pd.DataFrame:
        logging.info(f"Iniciando a extração do arquivo: {self.caminho_csv}")
        try :
            df = pd.read_csv(self.caminho_csv)
            logging.info("Extração concluida com sucesso.")
            return df
        except FileNotFoundError:
            logging.error(f"Arquivo não encontrado no caminho {self.caminho_csv}")
            return None
    
    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        if df is None:
            logging.warning("Transformação abortada: Nenhum dado foi extraido.")
            return None
        
        logging.info("Iniciando a transformação de dados...")

        df_limpo = df.dropna()

        df_limpo['nome_cliente'] = df_limpo['nome_cliente'].str.upper()

        logging.info(f"Transformação concluída. {len(df_limpo)} linhas processadas.")
        return df_limpo
    
    def carregar(self, df: pd.DataFrame, nome_tabela: str):
        if df is None:
            logging.warning("Carga abortada: Não há dados processados para salvar.")
            return
        
        logging.info(f"Conectando ao banco e salvando na tabela '{nome_tabela}'...")

        try:
            df.to_sql(nome_tabela, self.engine, if_exists= 'replace', index=False)
            logging.info("Dados salvos com sucesso! Pipeline finalizado.")
        except Exception as erro:
            logging.error(f"Ocorreu um erro ao salvar o bando de dados: {erro}")


if __name__ == "__main__":
    load_dotenv()
    
    usuario = os.getenv('DB_USER')
    senha = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    porta = os.getenv('DB_PORT')
    banco = os.getenv('DB_NAME')

    DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
    arquivo = os.path.join(DIRETORIO_ATUAL, 'data', 'dados_volumosos.csv')
    
    conexao_postgres = f"postgresql://{usuario}:{senha}@{host}:{porta}/{banco}"

    meu_pipeline = PipelineETL(arquivo, conexao_postgres)

    dados_brutos = meu_pipeline.extrair()
    dados_tratados = meu_pipeline.transformar(dados_brutos)
    
    meu_pipeline.carregar(dados_tratados, 'clientes_limpos')




