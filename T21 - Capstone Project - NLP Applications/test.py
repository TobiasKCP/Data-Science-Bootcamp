import spacy
import pandas as pd

nlp = spacy.load('en_core_web_sm')

texts = [('the','cheeseburger','was','great'),
         ('i','never','did','like','the','pizzas','too','much'), 
         ('yellowed','submarines','was','only','an','ok','song')]

df = pd.DataFrame({'word_tokens': texts})

def to_doc(words:tuple) -> spacy.tokens.Doc:
    # Create SpaCy documents by joining the words into a string
    return nlp(' '.join(words))

def remove_stops(doc) -> list:
    # Filter out stop words by using the `token.is_stop` attribute
    return [token.text for token in doc if not token.is_stop]

def lemmatize(doc) -> list:
    # Take the `token.lemma_` of each non-stop word
    return [token.lemma_ for token in doc if not token.is_stop]

# create documents for all tuples of tokens
docs = list(map(to_doc, df.word_tokens))

# apply removing stop words to all
df['removed_stops'] = list(map(remove_stops, docs))

# apply lemmatization to all
df['lemmatized'] = list(map(lemmatize, docs))

print(df)