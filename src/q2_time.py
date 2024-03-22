from typing import List, Tuple
from collections import defaultdict, Counter
from extract_emojis import extract_emojis
import pandas as pd


def q2_time(df: pd.DataFrame) -> List[Tuple[str, int]]:
    """
    Encuentra los top 10 emojis más usados y la cantidad de veces que se utilizan.
    
    Args:
    df (pd.DataFrame): DataFrame que contiene los datos del archivo JSON.
    
    Returns:
    List[Tuple[str, int]]: Lista de tuplas que contiene el emoji y la cantidad de veces que se utiliza.
    """
    # Inicializar un contador para almacenar la frecuencia de cada emoji
    emoji_frequency = Counter()
    
    # Iterar sobre las columnas relevantes del DataFrame
    for tweet_text in df['content']:
        # Extraer emojis del texto del tweet y actualizar el contador
        emojis_found = extract_emojis(tweet_text)
        emoji_frequency.update(emojis_found)
    
    # Obtener los 10 emojis más comunes
    top_10_emojis = emoji_frequency.most_common(10)
    
    return top_10_emojis


