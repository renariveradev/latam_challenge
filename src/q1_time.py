from typing import List, Tuple
from datetime import datetime
from load_json import cargar_datos_json
import pandas as pd

def q1_time(df: pd.DataFrame) -> List[Tuple[datetime.date, str]]:
    """
    Encuentra las top 10 fechas con más tweets y el usuario con más tweets para cada una de esas fechas.
    
    Args:
    df (pd.DataFrame): DataFrame que contiene los datos del archivo JSON.
    
    Returns:
    List[Tuple[datetime.date, str]]: Lista de tuplas que contiene la fecha y el usuario con más tweets.
    """
    # Convertir la columna 'date' a tipo datetime y extraer solo la fecha
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Obtener las top 10 fechas con más tweets
    top_10_dates = df['date'].value_counts().nlargest(10).index

    # Inicializar la lista para almacenar el resultado
    result = []

    # Iterar sobre las top 10 fechas
    for date in top_10_dates:
        # Filtrar el DataFrame para la fecha actual
        df_date = df[df['date'] == date]
        
        # Obtener el usuario con más tweets para esta fecha
        top_user = df_date['user'].apply(lambda x: x['username']).value_counts().idxmax()
        
        # Agregar la tupla (fecha, usuario) al resultado
        result.append((date, top_user))
    
    return result