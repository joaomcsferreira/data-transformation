import json
import pandas as pd

# Função para carregar os dados JSON
def carregar_json(arquivo_json):
    with open(arquivo_json, 'r', encoding='utf-8') as f:
        dados_json = json.load(f)
    return dados_json

# Função para carregar os dados CSV
def carregar_csv(arquivo_csv):
    dados_csv = pd.read_csv(arquivo_csv, sep=',', dtype=str)
    return dados_csv

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

# Função para adicionar informações do CSV ao JSON
def adicionar_info_json(dados_json, dados_csv):
    # Criar um dicionário de mapeamento a partir do CSV
    mapeamento_csv = dados_csv.set_index('Cod').to_dict(orient='index')

    # Iterar sobre as features do JSON e adicionar informações do CSV
    for feature in dados_json['features']:
        cd_mun = feature['properties']['cd_mun']
        if cd_mun in mapeamento_csv:
            # Adicionar todas as informações do CSV ao JSON
            for chave, valor in mapeamento_csv[cd_mun].items():
                feature['properties'][chave] = valor.strip()
                

    return dados_json

# Função para salvar o JSON atualizado
def salvar_json(dados_json, arquivo_json):
    with open(arquivo_json, 'w', encoding='utf-8') as f:
        json.dump(dados_json, f, ensure_ascii=False, indent=4)

# Caminhos dos arquivos
arquivo_json = 'csv/municipios.json'
arquivo_csv = 'csv/data.csv'
arquivo_json_atualizado = 'municipios.json'

# Carregar dados
dados_json = carregar_json(arquivo_json)
dados_csv = carregar_csv(arquivo_csv)

# Adicionar informações do CSV ao JSON
dados_json_atualizado = adicionar_info_json(dados_json, dados_csv)

# Salvar o JSON atualizado
salvar_json(dados_json_atualizado, arquivo_json_atualizado)

print("Informações adicionadas e JSON atualizado salvo com sucesso.")
