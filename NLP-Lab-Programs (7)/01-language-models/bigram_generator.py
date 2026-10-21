# Aim: Generate bigrams from a sentence.
# Algorithm:
# 1. Split the sentence into words.
# 2. Form pairs of adjacent words.
# 3. Display each pair.

text = "I love natural language processing"
words = text.split()

for i in range(len(words) - 1):
    print((words[i], words[i + 1]))
