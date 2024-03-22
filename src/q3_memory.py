from typing import List, Tuple
import pandas as pd
from memory_profiler import profile

@profile
def q3_memory(df: pd.DataFrame) -> List[Tuple[str, int]]:
    # Inicializar un diccionario para almacenar el conteo de menciones de cada usuario
    mention_count = {}
    
    # Iterar sobre cada fila del DataFrame
    for index, row in df.iterrows():
        # Obtener la lista de usuarios mencionados en el tweet
        mentions = row['mentionedUsers']
        if mentions:
            # Iterar sobre cada usuario mencionado y actualizar su conteo
            for user in mentions:
                username = user['username']
                mention_count[username] = mention_count.get(username, 0) + 1
    
    # Ordenar el diccionario por los conteos de menciones en orden descendente
    sorted_mentions = sorted(mention_count.items(), key=lambda x: x[1], reverse=True)
    
    # Tomar los 10 usuarios más mencionados
    top_10_mentions = sorted_mentions[:10]
    
    return top_10_mentions