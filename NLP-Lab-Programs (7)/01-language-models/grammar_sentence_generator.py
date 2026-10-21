# Aim: Generate grammatically structured sentences.
# Algorithm:
# 1. Define subjects, verbs, and objects.
# 2. Combine each subject, verb, and object.
# 3. Display the sentences.

subjects = ["The boy", "The girl"]
verbs = ["reads", "likes"]
objects = ["a book", "Python"]

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            print(subject, verb, obj)
