# import itertools
# a = list(itertools.permutations(['A','B','C']))
# print(a)

string_final = []
k = 0
def perm(a):  
    global k
    if k == len(a):
        listToStr = ''.join([str(elem) for elem in a])
        string_final.append(listToStr)

    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i], a[k]
            k += 1 
            perm(a)
            k -= 1
            a[k], a[i] = a[i], a[k]
    return ' '.join([str(elem) for elem in string_final])

string_input = input()
list_input = []
for i in string_input:
    list_input.append(i)
print(perm(list_input))