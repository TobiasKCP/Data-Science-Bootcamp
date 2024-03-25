#This is a program which compares words and sentences.

import spacy


nlp = spacy.load('en_core_web_md')


# Comparing singular words.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print('------Comparing Words------')
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


#Comparing words in a sentance.
tokens = nlp('cat apple monkey banana')

print('------Comparing Words In A Sentance------')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text,token2.text,token1.similarity(token2))


# Comparing sentances
sentence_to_compare = "Why is my cat on the car"

sentences=["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

print('------Comparing sentances------')
for sentence in sentences:
    similarity=nlp(sentence).similarity(model_sentence)
    print(sentence + "-" + str(similarity))

# ---- Comparing en_core_web_sm and en_core_web_md ----    

# Using en_core_web_sm give the following warning message
'''UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements.
This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. 
You can always add your own word vectors, or use one of the larger models instead if available.'''
# Word vectors are a unique numerical values assigned to words where the value can be used as a point of comparison between words. Meaning similar words have similar values.
# The lack of these vectors cause an overestimation in similarity between individual words and underestimation when comparing whole sentences.

#Variable with the description of the film that has been watched.
watched_movie = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk in to a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
movie_to_compare= nlp(watched_movie)

# Reading in movies.txt
# Couldn't get releative path to work

file = open(r"T20 - NLP - Semantic Similarity\14-002 NLP - Semantic Similarity\movies.txt", "r")
movies = file.readlines()
file.close

# Function which compares the descriptions of movies.

def movie_select(movies_to_comp, movie_to_compare):
    score = 0
    for movie in movies_to_comp:
        similarity = nlp(movie).similarity(movie_to_compare)
        if similarity > score:
            score = similarity
            movie_to_watch = movie
    print("\nBased of the movie you watched you should watch: " + movie_to_watch[:7] + "\n\ndescription:\n" + movie_to_watch[9:])
    return

#Calling the user define function "movie_select" and passing the relevant variables.
movie_select(movies, movie_to_compare)




