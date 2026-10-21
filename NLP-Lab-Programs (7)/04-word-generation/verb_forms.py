# Aim: Display common verb forms using lemma-plus-tag notation.
verb_forms = {
    "write+VBD": "wrote",
    "write+VBN": "written",
    "stop+VBG": "stopping",
    "study+VBZ": "studies",
    "die+VBG": "dying",
    "play+VBD": "played"
}

for tag, form in verb_forms.items():
    print(tag, "->", form)
