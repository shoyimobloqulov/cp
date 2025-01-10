def filter_list(lst, n):
    if n != 0:
        return [x for x in lst if x % 2 == 0]
    else:
        return [x for x in lst if x % 2 != 0]
print(filter_list([1,2,3,4,5,6],0))