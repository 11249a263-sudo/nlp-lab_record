# Aim: Calculate tokens, types, and type-token ratio.
text = "The cat sat on the mat. The dog sat on the log."
words = text.replace(".", "").split()

tokens = len(words)
types_lower = len(set(word.lower() for word in words))
types_case_preserved = len(set(words))
ttr = types_lower / tokens if tokens else 0

print("Tokens =", tokens)
print("Types (lowercase) =", types_lower)
print("Types (case preserved) =", types_case_preserved)
print("TTR =", round(ttr, 2))
