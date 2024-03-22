import pandas as pd
import json

def cargar_datos_json(file_path: str) -> pd.DataFrame:
    """
    Carga los datos de un archivo JSON en un DataFrame de pandas.
    
    Args:
    file_path (str): Ruta del archivo JSON.
    
    Returns:
    pd.DataFrame: DataFrame que contiene los datos del archivo JSON.
    

    # Inicializa una lista para almacenar los objetos JSON
    data = []
    
    # Abre el archivo JSON en modo lectura
    with open(file_path, "r") as file:
        # Lee cada línea del archivo
        for line in file:
            # Intenta cargar la línea como un objeto JSON y añádelo a la lista
            try:
                json_data = json.loads(line)
                data.append(json_data)
            except json.JSONDecodeError as e:
                print(f"Error al decodificar JSON: {e}")

    # Convierte la lista de objetos JSON en un DataFrame de pandas
    #df = pd.DataFrame(data)
    return data
    """
    try:
        # Leer el archivo JSON directamente en un DataFrame
        df = pd.read_json(file_path, lines=True)
        return df
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
    return pd.DataFrame()
    