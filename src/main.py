import pandas as pd
import geojson
from math import isnan

def csv_to_geojson(csv_file_path, geojson_file_path, lat_col, lon_col):
    # Ler o arquivo CSV
    df = pd.read_csv(csv_file_path, delimiter=',')  # Adicionando delimitador correto
    
    # Verificar se as colunas estão presentes no DataFrame
    if lat_col not in df.columns or lon_col not in df.columns:
        raise ValueError(f"Colunas especificadas não encontradas no CSV. Colunas disponíveis: {df.columns}")

    # Lista para armazenar os pontos GeoJSON
    features = []

    # Iterar sobre as linhas do DataFrame
    for _, row in df.iterrows():
        # Verificar e substituir NaN por None
        lat = row[lat_col]
        lon = row[lon_col]
        lat = None if pd.isna(lat) else lat
        lon = None if pd.isna(lon) else lon
        
        # Criar um objeto Point GeoJSON se ambos lat e lon são válidos
        if lat is not None and lon is not None:
            point = geojson.Point((lon, lat))
        else:
            point = None

        # Criar um objeto Feature GeoJSON
        properties = {key: (None if pd.isna(value) else value) for key, value in row.items()}
        feature = geojson.Feature(geometry=point, properties=properties)

        # Adicionar o objeto Feature à lista de features
        features.append(feature)

    # Criar o objeto FeatureCollection GeoJSON
    feature_collection = geojson.FeatureCollection(features)

    # Salvar o FeatureCollection em um arquivo GeoJSON
    with open(geojson_file_path, 'w') as f:
        geojson.dump(feature_collection, f, indent=2)


csv_file_path = 'csv/base_minerios_municipios.csv' 
geojson_file_path = 'geojson/base_minerios_municipios.geojson'
lat_col = 'lat'  
lon_col = 'lon' 

csv_to_geojson(csv_file_path, geojson_file_path, lat_col, lon_col)
