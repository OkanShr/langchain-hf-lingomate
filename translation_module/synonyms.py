import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')

# Get synonyms of a word using WordNet
def get_synonyms(word):
    synonyms = set()
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace('_', ' '))
    return list(synonyms)
