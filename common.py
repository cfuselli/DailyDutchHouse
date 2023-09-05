import re

def get_price(text):

    text = text.split(",")[0]
    text = re.sub(r'\D', '', text)

    return int(text)
            
