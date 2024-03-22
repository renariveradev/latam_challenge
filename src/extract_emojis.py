import regex as re

def extract_emojis(text):
    """
    Extrae los emojis de un texto dado.
    
    Args:
    text (str): El texto del cual se extraerán los emojis.
    
    Returns:
    List[str]: Lista de emojis extraídos.
    """
    emoji_pattern = re.compile(r'\p{So}')  # Unicode property escapes for emojis
    emojis = emoji_pattern.findall(text)
    return emojis