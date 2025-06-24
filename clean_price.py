def clean_price(text):
    if not isinstance(text, str):
        return None

  
    start = text.index('R$')
    price_part = text[start + 2:].strip() 
    
    allowed_chars = '0123456789.,'
    cleaned = ''.join(c for c in price_part if c in allowed_chars)
    
    cleaned = cleaned.replace('.', '').replace(',', '.')
    
    try:
        return float(cleaned)
    except ValueError:
        return None