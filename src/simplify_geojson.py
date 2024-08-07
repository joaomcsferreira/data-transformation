import geopandas as gpd
from shapely.geometry import shape
from shapely.geometry import mapping
import json


def simplify_geojson(input_file, output_file, tolerance=0.01):
    # Carregar o arquivo GeoJSON
    gdf = gpd.read_file(input_file)

    # Simplificar as geometrias
    gdf["geometry"] = gdf["geometry"].simplify(tolerance)

    # Remover todas as colunas não essenciais
    gdf = gdf[["geometry"]]

    # Salvar o GeoDataFrame simplificado como GeoJSON
    gdf.to_file(output_file, driver="GeoJSON")


if __name__ == "__main__":
    input_file = "geojson/linha_alta_tensao.json"
    output_file = "result/linha_alta_tensao.json"
    tolerance = 0.1  # Ajuste a tolerância conforme necessário

    simplify_geojson(input_file, output_file, tolerance)
    print(f"Arquivo simplificado salvo em {output_file}")

    # import geopandas as gpd

    # def simplify_geojson(input_file, output_file, tolerance):
    #     # Carregar o arquivo GeoJSON
    #     gdf = gpd.read_file(input_file)

    #     # Simplificar as geometrias
    #     gdf["geometry"] = gdf["geometry"].simplify(tolerance)

    #     # Remover todas as colunas não essenciais
    #     gdf = gdf[["geometry"]]

    #     # Salvar o GeoDataFrame simplificado como GeoJSON
    #     gdf.to_file(output_file, driver="GeoJSON")

    # if __name__ == "__main__":
    #     input_file = "geojson/ish.json"
    #     output_file = "result/ish.json"

    #     # Comece com um valor de tolerância maior
    #     tolerance = 0.01  # Ajuste este valor conforme necessário

    #     simplify_geojson(input_file, output_file, tolerance)
    print(f"Arquivo simplificado salvo em {output_file}")
