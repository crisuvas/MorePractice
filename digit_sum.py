def digit_sum(x):
    total = 0
    while x > 0:
        total += x
        x -= 1
    return total


print(digit_sum(10))
