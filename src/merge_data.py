import pandas as pd


def sum_rows():
    # Função para ler o arquivo CSV e realizar as operações solicitadas
    def processar_csv(file_path):
        # Lendo o arquivo CSV
        df = pd.read_csv(file_path)

        # Realizando o somatório da coluna 'População residente (Pessoas)' e mantendo os últimos registros dos outros campos
        df_agrupado = (
            df.groupby("Cód.")
            .agg(
                {
                    "População residente (Pessoas)": "sum",
                    "Município": "last",  # Substitua 'OutroCampo1' pelo nome real da coluna
                    "Idade": "last",  # Substitua 'OutroCampo2' pelo nome real da coluna
                    "Ano": "last",  # Substitua 'OutroCampo2' pelo nome real da coluna
                    # Adicione mais campos conforme necessário
                }
            )
            .reset_index()
        )

        return df_agrupado

    # Exemplo de uso
    file_path = (
        "csv/pop-residente-2022.csv"  # Substitua pelo caminho do seu arquivo CSV
    )
    df_resultado = processar_csv(file_path)

    # Salvando o resultado em um novo arquivo CSV
    df_resultado.to_csv("resultado.csv", index=False)

    print("Arquivo processado e salvo como 'resultado.csv'.")


def merge_by_id():
    # Ler os três arquivos CSV
    df1 = pd.read_csv("csv/ok/idhm-2010.csv")
    df3 = pd.read_csv("csv/ok/merged_arquivo.csv")

    # Fazer o merge dos dataframes com base na coluna 'Cod'
    merged_df = df1.merge(df3, on="Nome do Município")

    # Salvar o resultado em um novo arquivo CSV
    merged_df.to_csv("merged_arquivo.csv", index=False)

    # Exibir o dataframe resultante
    print(merged_df)


def remove_columns_from_csv(input_csv, output_csv, columns_to_remove):
    """
    Remove colunas específicas de um arquivo CSV e salva o resultado em um novo arquivo.

    Parameters:
    input_csv (str): O caminho para o arquivo CSV de entrada.
    output_csv (str): O caminho para o arquivo CSV de saída.
    columns_to_remove (list): Lista de nomes de colunas a serem removidas.
    """
    # Ler o arquivo CSV
    df = pd.read_csv(input_csv)

    # Remover as colunas especificadas
    df.drop(columns=columns_to_remove, inplace=True)

    # Salvar o resultado em um novo arquivo CSV
    df.to_csv(output_csv, index=False)

    # Retornar o DataFrame resultante (opcional)
    return df


# Exemplo de uso da função
input_csv = "csv/data.csv"
output_csv = "output_arquivo.csv"
columns_to_remove = []

# Chamar a função
df_resultante = remove_columns_from_csv(input_csv, output_csv, columns_to_remove)

# Exibir o DataFrame resultante
print(df_resultante)
