list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
n = 0
list_sum = []
for equals in list1:
    n1 = list1[n]
    n2 = list2[n]
    summ = n1 * n2
    list_sum.append(summ)
    n += 1
print(list_sum)
