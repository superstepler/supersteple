squn = 1,1,1,2,3,3,4,5,5,5,6,7,8,9
def unt_it(squn):
    dict_1 = {}
    for num in squn:
        if num in dict_1.keys():
            dict_1[num] += 1
        else:
            dict_1[num] = 1
    dict_2 = {}
    max_1 = max(dict_1, key=dict_1.get)
    dict_2[max_1] = dict_1[max_1]
    del dict_1[max_1]
    max_2 = max(dict_1, key=dict_1.get)
    dict_2[max_2] = dict_1[max_2]
    del dict_1[max_2]
    max_3 = max(dict_1, key=dict_1.get)
    dict_2[max_3] = dict_1[max_3]
    del dict_1[max_3]
    return dict_2
print(unt_it(squn))


