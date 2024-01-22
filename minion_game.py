def minion_game(s):
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    length = len(s)

    for i in range(length):
        if s[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


string_s = "BANANA"
minion_game(string_s)