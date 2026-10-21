# Aim: Generate plural forms of common nouns.
irregular = {
    "child": "children",
    "knife": "knives"
}

words = ["box", "city", "child", "boy", "bus", "knife"]

for word in words:
    if word in irregular:
        plural = irregular[word]
    elif word.endswith("y") and len(word) > 1 and word[-2].lower() not in "aeiou":
        plural = word[:-1] + "ies"
    elif word.endswith(("s", "x", "z", "ch", "sh")):
        plural = word + "es"
    else:
        plural = word + "s"
    print(word, "->", plural)
