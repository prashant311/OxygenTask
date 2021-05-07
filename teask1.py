a = [1, [2, 3, [4, 5, 6], [7, [8, 9, [10, 11], 12]]]]
b = []


def removeNest(li):
    for i in li:
        if type(i) == list:
            removeNest(i)
        else:
            b.append(i)


removeNest(a)
print(b)