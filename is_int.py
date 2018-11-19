def is_int(x):
    absolute_count = abs(x)
    type_count = type(x)
    round_count = round(absolute_count)
    if type_count == int and absolute_count - round_count == 0:
        return True
    else:
        return False


print(is_int(32.4))
