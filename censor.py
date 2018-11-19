def censor(text, word):
    hack = ""
    for _ in word:
        hack += "*"
    new_word = ""
    for j in range(len(text.split())):
        if text.split()[j] == word:
            new_word += hack
        else:
            new_word += str(text.split()[j])
        new_word += " "
    return new_word


print(censor("hey hey hey", "hey"))
