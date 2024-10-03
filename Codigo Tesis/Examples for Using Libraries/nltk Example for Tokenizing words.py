# nltk Example for Tokenizing words

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text
text = "Natural Language Processing with NLTK in Python"

# Tokenize and tag
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

print(tagged)
