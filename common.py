import spacy
import re

nlp = spacy.load("en_core_web_sm")

def get_price(text):

    # doc = nlp(text)

    # final = 0 

    # prices = []
    # for ent in doc.ents:
    #     if ent.label_ == "MONEY":  # MONEY is spaCy's label for monetary values

    #         val = ent.text.split(",")[0].replace(".",'')
    #         prices.append(int(val))

    # for p in prices:
    #     if p > 0 and p<500000:
    #         final = p

    text = text.split(",")[0]
    text = re.sub(r'\D', '', text)

    return int(text)
            
