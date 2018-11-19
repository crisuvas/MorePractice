def reverse(text):
    word = ""
    large = len(text)
    while large > 0:
        word += text[large - 1]
        large -= 1
    return word


print(reverse("Cris"))
