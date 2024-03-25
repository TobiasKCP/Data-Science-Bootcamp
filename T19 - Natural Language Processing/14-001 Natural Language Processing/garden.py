# This is a program that tokenizes a list of gardenpathsentances and performs named entity recognition.

import spacy

nlp = spacy.load('en_core_web_sm')


#list of garden path sentences

gardenpathsentences = ['While Tom was washing the dishes fell on the floor.', 'The sour drink from the ocean.', 'Mary gave the child a Band-Aid.', 'That Jill is never here hurts.', 'The cotton clothing is made of grows in Mississippi.']

#Tokenization and name entity recognition iterating over the list.

for x in gardenpathsentences:
    print(x)
    doc = nlp(x)
    print([token.orth_ for token in doc if not token.is_punct | token.is_space])
    print([(i, i.label_, i.label) for i in doc.ents])

print(spacy.explain('GPE'))
print(spacy.explain('PERSON'))

# 'GPE' represents Countries Cities and States.
# The GPE entity was incorrectly assigned as the sentence refers to the river not the state.

# 'PERSON' simply represents a person
# The entity was correctly assigned in all cases