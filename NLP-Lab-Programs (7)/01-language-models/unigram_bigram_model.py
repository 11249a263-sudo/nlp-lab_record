# Aim: Count word/bigram frequencies and calculate simple probabilities.
from collections import Counter

sentences = [
    "I like NLP",
    "I like Python",
    "I study NLP"
]

words = " ".join(sentences).split()
unigrams = Counter(words)
bigrams = Counter((words[i], words[i + 1]) for i in range(len(words) - 1))

print("Word Frequencies")
for word, count in unigrams.items():
    print(word, count)

print("\nBigram Frequencies")
for pair, count in bigrams.items():
    print(pair, count)

print("\nUnigram Probabilities")
for word, count in unigrams.items():
    print(word, round(count / len(words), 3))

print("\nBigram Conditional Probabilities")
for (first, second), count in bigrams.items():
    print((first, second), round(count / unigrams[first], 3))
