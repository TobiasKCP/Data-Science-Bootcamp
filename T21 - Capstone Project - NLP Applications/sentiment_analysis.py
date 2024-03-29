
#Importing relevant modules

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd

nlp = spacy.load("en_core_web_md")
nlp.add_pipe('spacytextblob')

# Getting the data from the relevant cvs file.

review_data = pd.read_csv(r"T21 - Capstone Project - NLP Applications\amazon_product_reviews - reduced.csv", low_memory=False)
clean_data = review_data.dropna(subset=['reviews.text'])
reviews = pd.DataFrame({'original_text':clean_data['reviews.text']})
print(reviews)

# Asking the user how many reviews they would like to analyse
# and deleting values in the dataframe "reviews" which are not been analyzed to speed up runtime.

x = 0
while x == 0:
    try: text_to_check = int(input("how many reviews would you like to check: "))
    except ValueError: print("Unexpected error please make sure you enter a integer")

    if text_to_check <= len(reviews):

        reviews = reviews.iloc[:text_to_check]
        x = 1
    else:
        print("please enter a value between 1 and " + str(len(reviews)))

# Preprocessing the text data by removing stop words and lemmatization.

def to_doc(words:tuple) -> spacy.tokens.Doc:
    return nlp(words)

# Filter out stop words by using the `token.is_stop` attribute
def remove_stops(doc) -> list:
    return [token.text for token in doc if not token.is_stop]

    # Take the `token.lemma_` of each non-stop word
def lemmatize(doc) -> list:
    return [token.lemma_ for token in doc if not token.is_stop]

# create documents for all tuples of tokens
docs = list(map(to_doc, reviews.original_text))

# apply removing stop words to all
reviews['removed_stops'] = list(map(remove_stops, docs))

# apply lemmatization to all
reviews['lemmatized'] = list(map(lemmatize, docs))

#Function which predicts a reviews sentiment.
def pre_sent(df, column, row):
    doc = df[column][row]
    if isinstance(doc, list):
        doc = ' '.join(doc)
    doc = nlp(str(doc))
    sent = doc._.blob.polarity
    return sent

sentiment_base = []
sentiment_removed_stop = []
sentiment_lemmatized = []

# For loop that calls the function to predict the sentiment of review
for i in range(0, text_to_check):
    
    sentiment_base.append(pre_sent(reviews, 'original_text', i))
    sentiment_removed_stop.append(pre_sent(reviews, 'removed_stops', i))
    sentiment_lemmatized.append(pre_sent(reviews, 'lemmatized', i))

# Storing the results back in the data frame
reviews['sentiment_base'] = sentiment_base
reviews['sentiment_removed_stop'] = sentiment_removed_stop
reviews['sentiment_lemmatized'] = sentiment_lemmatized

 
print(reviews)

# While loop to allow the user to look specific entries in the dataframe and compare the similarity of reviews.
while x == 1:
    user_decision = str(input("\n Would you like to look at a specific review or compare two reviews for similarity. \n Enter: \n 'R' to look a specific review \n 'S' to check the similarity between two reviews \n 'N' to exit the program \n -"))
    if user_decision == 'N':
        print("exiting program")
        x = 0
        reviews.to_excel('reviews_out.xlsx')
        
    elif user_decision == 'R':
        selected = int(input("Please enter the index of the review you would like to view: "))
        print(" ")
        print(reviews.loc[[selected]])
        print(" ")

    elif user_decision == 'S':
        try: to_comp1 = int(input("Please enter the index of one of the reviews you would like to compare: ")) 
        except ValueError: print("Please enter a integer")

        try: to_comp2 = int(input("Please enter the index of one of the reviews you would like to compare: "))
        except ValueError: print("Please enter a integer")

        to_comp1 = nlp(str(reviews['original_text'][to_comp1]))
        print("text 1: " + str(to_comp1))
        to_comp2 = nlp(str(reviews['original_text'][to_comp2]))
        print("text 2: " + str(to_comp2))
        print("The similarity is: "+ str(to_comp1.similarity(to_comp2)))

    else:
        print("Please select a valid option")

