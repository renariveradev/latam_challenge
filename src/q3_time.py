from typing import List, Tuple
import pandas as pd
from collections import Counter


def q3_time(df: pd.DataFrame) -> List[Tuple[str, int]]:
    # Inicializar un contador para almacenar el conteo de menciones de cada usuario
    mention_count = Counter()
    
    # Obtener todas las menciones de usuarios en una lista
    all_mentions = df['mentionedUsers'].explode().dropna()
    
    # Contar las menciones de usuarios y almacenar el resultado en el contador
    mention_count.update(all_mentions.apply(lambda x: x['username']))
    
    # Obtener los 10 usuarios más mencionados
    top_10_mentions = mention_count.most_common(10)
    
    return top_10_mentions