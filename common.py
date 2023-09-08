import re

def get_price(text):

    text = text.split(",")[0]
    text = re.sub(r'\D', '', text)

    if len(text) == 0:
        return 0
    
    if len(text) == 8:
        text = text[:4]

    return int(text)
            
