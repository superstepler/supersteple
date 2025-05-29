lst = [1, 2, 3, 4]
def change(lst):
    lst[-1], lst[0] = lst[0], lst[-1]
    return lst
print(change(lst))