# Aim: Perform Part-of-Speech tagging using NLTK.
# Install: pip install nltk
# NLTK may require tokenizer/tagger data downloads for your installed version.

import nltk

sentence = "The student studies natural language processing"
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

for word, tag in tagged:
    print(word, "->", tag)
