class Student : 
    def __init__(self,stt,masv, score):
        self.stt = stt
        self.masv = masv
        self.score = score
    def __repr__(self):
        return str(dict({
            "stt": self.stt,
            "masv" : self.masv,
            "score" : self.score,
        }))

students = []
dic_students = dict()
f = open("TongHopDiem.csv", 'r',encoding="utf-8")
# lưu ý là encoding utf 8 sẽ gây ra lỗi còn unicode_escapse sẽ ko có lỗi 
listoflines = f.readlines()
i = 0
for line in listoflines:
    #print(line) 
    if i == 0 : 
        i = 1
        continue
    x = line.split(",")
    students.append(Student(stt = x[0],masv = x[1], score= float(x[2].replace('\n','')))) # add to list 
    dic_students[x[1]] =  Student(stt = x[0], masv = x[1], score= float(x[2].replace('\n','')))

A = 0
B = 0 
C = 0
D = 0
F = 0
for student in dic_students:
    if dic_students[student].score >= 8.5 : 
        A += 1 
    elif 8.5 > dic_students[student].score >= 7.0:
        B += 1
    elif 7 > dic_students[student].score >= 5.5 : 
        C += 1 
    elif 5.5 > dic_students[student].score >= 4.0 :
        D += 1 
    else : 
        F += 1 
    print(dic_students[student].masv, dic_students[student].score)

print(A)
print(B)
print(C)
print(D)
print(F)