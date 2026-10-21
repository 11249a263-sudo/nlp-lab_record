# Aim: Accept the string "ab" using a simple DFA.
# States: 0 = start, 1 = after reading 'a', 2 = accepting state.

string = "ab"
state = 0

for char in string:
    if state == 0 and char == "a":
        state = 1
    elif state == 1 and char == "b":
        state = 2
    else:
        state = -1
        break

print("Accepted" if state == 2 else "Rejected")
