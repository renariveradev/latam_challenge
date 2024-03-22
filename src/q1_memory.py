from typing import List, Tuple
from datetime import datetime
#from load_json import cargar_datos_json
from memory_profiler import profile

import pandas as pd

@profile
def q1_memory(df: pd.DataFrame) -> List[Tuple[datetime.date, str]]:
    """
    Encuentra las top 10 fechas con más tweets y el usuario con más tweets para cada una de esas fechas.
    
    Args:
    file_path (str): Ruta del archivo JSON.
    
    Returns:
    List[Tuple[datetime.date, str]]: Lista de tuplas que contiene la fecha y el usuario con más tweets.
    """
    # Cargar datos JSON en un DataFrame
    #df = pd.DataFrame(cargar_datos_json(file_path))

    # Convertir la columna 'date' a tipo datetime
    #df['date'] = pd.to_datetime(df['date'])
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Obtener las top 10 fechas con más tweets
    #top_10_fechas = df['date'].dt.date.value_counts().head(10).index
    top_10_fechas = df['date'].value_counts().nlargest(10).index

    resultados = []
    """
    # Crear un DataFrame auxiliar para agrupar por fecha y usuario
    aux_df = df.groupby(['date', df['user'].apply(lambda x: x['username'])]).size().reset_index(name='count')

    # Encontrar el usuario con más tweets para cada fecha
    max_tweets_idx = aux_df.groupby('date')['count'].idxmax()
    top_users = aux_df.loc[max_tweets_idx]

    # Crear la lista de resultados
    resultados = list(zip(top_users['date'], top_users['user']))
    """
    
    # Para cada una de las top 10 fechas, obtener el usuario (username) que más publicaciones tiene
    for fecha in top_10_fechas:
        #tweets_en_fecha = df[df['date'].dt.date == fecha]
        tweets_en_fecha = df[df['date'] == fecha]
        usuario_mas_tweets = tweets_en_fecha['user'].apply(lambda x: x['username']).value_counts().idxmax()
        resultados.append((fecha, usuario_mas_tweets))
    
    #resultados = pd.DataFrame(resultados, columns=['Fecha', 'Usuario con más Tweets'])
    return resultados