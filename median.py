def median(old_list):
    old_list = sorted(old_list)
    count = len(old_list)/ 2.0
    if count % 1 != 0:
        count = int(round(count)) - 1
        return old_list[count]
    else:
        count = int(round(count)) - 1
        count2 = count + 1
        total = (old_list[count] + old_list[count2]) / 2
        return total


print(median([4, 2, 5, 12]))
