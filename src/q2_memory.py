from typing import List, Tuple
from collections import defaultdict, Counter
from extract_emojis import extract_emojis

from memory_profiler import profile

import pandas as pd


@profile
def q2_memory(df: pd.DataFrame) -> List[Tuple[str, int]]:
    """
    Encuentra los top 10 emojis más usados, la cantidad de veces que se utilizan y el nombre del usuario que lo utilizó.
    
    Args:
    df (pd.DataFrame): DataFrame que contiene los datos del archivo JSON.
    
    Returns:
    List[Tuple[str, int]]: Lista de tuplas que contiene el emoji y la cantidad de veces que se utiliza.
    """
    # Inicializar un diccionario para almacenar la frecuencia de cada emoji
    emoji_frequency = Counter()
    
    # Iterar sobre las filas del DataFrame
    for index, row in df.iterrows():
        # Obtener el texto del tweet
        tweet_text = row['content']
        
        # Extraer emojis del texto del tweet y actualizar el contador
        emojis_found = extract_emojis(tweet_text)
        emoji_frequency.update(emojis_found)
    
    # Obtener los 10 emojis más comunes
    top_10_emojis = emoji_frequency.most_common(10)
    
    return top_10_emojis