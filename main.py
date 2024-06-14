import pandas as pd
import geojson

def csv_to_geojson(csv_file_path, geojson_file_path, lat_col, lon_col):
    df = pd.read_csv(csv_file_path, delimiter=';')  
    
    if lat_col not in df.columns or lon_col not in df.columns:
        raise ValueError(f"Colunas especificadas não encontradas no CSV. Colunas disponíveis: {df.columns}")

    features = []

    for _, row in df.iterrows():
        point = geojson.Point((row[lon_col], row[lat_col]))

        feature = geojson.Feature(geometry=point, properties=row.to_dict())

        features.append(feature)

    feature_collection = geojson.FeatureCollection(features)

    with open(geojson_file_path, 'w') as f:
        geojson.dump(feature_collection, f, indent=2)

csv_file_path = 'csv/Pontos_Turisticos_Piauí.csv' 
geojson_file_path = 'geojson/Pontos_Turisticos_Piauí.geojson'
lat_col = 'Latitude'  
lon_col = 'Longitude' 

csv_to_geojson(csv_file_path, geojson_file_path, lat_col, lon_col)
