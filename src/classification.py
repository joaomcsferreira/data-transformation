import json

# Carregar o arquivo JSON gerado no código anterior
with open('json1_updated.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Criar dicionários vazios para cada classe de classificação
classifications = {'A': [], 'B': [], 'C': [], 'D': [], 'E': []}

# Organizar as features de acordo com a classificação
for feature in json_data['features']:
    classification = feature['properties']['Classificação']
    classifications[classification].append(feature)

# Salvar as features de cada classificação em arquivos separados
for classification, features in classifications.items():
    file_name = f'features_class_{classification}.json'
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump({'type': 'FeatureCollection', 'features': features}, f, ensure_ascii=False, indent=2)
    print(f'Arquivo {file_name} criado com sucesso.')

print('Separação concluída.')
