def anti_vowel(text):
    t = ""
    for c in text:
        for i in "aeiouAEIOU":
            if c == i:
                c = ""
            else:
                c = c
        t += c
    return t


print(anti_vowel("What are you doing"))
