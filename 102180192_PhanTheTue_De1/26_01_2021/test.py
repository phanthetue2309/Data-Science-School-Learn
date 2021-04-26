l = [[0, 1, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
l.sort(key=lambda x: x[2])
print(l)

l = [["tue",3,2],["nhan",2,4]]
l.sort(key=lambda x: x[2])  # lambda like an def return l[2]
print(l)
l.sort(key=lambda x: x[1])
print(l)
l.sort(key=lambda x: (x[0],x[1],x[2]))
print(l)