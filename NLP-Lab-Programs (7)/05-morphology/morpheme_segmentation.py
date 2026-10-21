# Aim: Segment words into morphemes.
words = {
    "unhappiness": ["un", "happy", "ness"],
    "teachers": ["teach", "er", "s"],
    "disestablishment": ["dis", "establish", "ment"],
    "internationalization": ["inter", "nation", "al", "ize", "ation"]
}

for word, parts in words.items():
    print(word, "->", " + ".join(parts), "| morphemes:", len(parts))
