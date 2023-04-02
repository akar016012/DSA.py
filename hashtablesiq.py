#check if two list have an item in common -
#naive approach - use 2 for loops (o(n^2))


def itemInCommon(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]
print(f'Naive Apporach: {itemInCommon(list1, list2)}')

#optimized approach - using hashtables O(n) 😊


def itemInCommonOpt(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False


list3 = [1, 3, 5]
list4 = [2, 4, 5]
print(f'Optimized Apporach: {itemInCommonOpt(list3, list4)}')
