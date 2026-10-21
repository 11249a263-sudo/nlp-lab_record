# Aim: Compare stemming and lemmatization with NLTK.
# Install: pip install nltk
# First run may need WordNet data: nltk.download("wordnet")

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

words = ["running", "ran", "runs", "studies", "played"]
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

for word in words:
    print(
        word,
        "-> stem:", stemmer.stem(word),
        "| lemma:", lemmatizer.lemmatize(word, pos="v")
    )
