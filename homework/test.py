def include_list(list):
    ansv = None
    for item in list:
        counts = list.count(item)
        if counts != 1:
            ansv = False
            break
        else:
            ansv = True
    return ansv


# list1 = [1, 2, 3]
# list2 = [1, 2, 3, 4, 4]
# list3 = [1, 1, 2, 3]
# print(include_list(list1))
# print(include_list(list2))
# print(include_list(list3))

def numbers(list):
    nums = []
    for item in list:
        nums.append(-item)
    return nums

list1 = [1, 2, 3]
print(numbers(list1))