def remove_duplicates(list_dup):
    new_list = []
    for i in list_dup:
        if i not in new_list:
            new_list.append(i)
    new_list.sort()
    return new_list


print(remove_duplicates([2, 2, 4, 6, 3, 2]))
