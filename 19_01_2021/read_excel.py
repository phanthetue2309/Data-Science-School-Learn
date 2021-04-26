class Student : 
    def __init__(self, id, name,date_of_birth, class_study):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.class_study = class_study
    def __repr__(self):
        return str(dict({
            "id": self.id,
            "name": self.name,
        }))
    
students = []
dic_students = dict()
f = open("Check.csv", 'r',encoding="unicode_escape")
# lưu ý là encoding utf 8 sẽ gây ra lỗi còn unicode_escapse sẽ ko có lỗi 
listoflines = f.readlines()
for line in listoflines:
    #print(line) 
    x = line.split(",")
    students.append(Student(id = x[1],name = x[2], date_of_birth = x[3] , class_study = x[4])) # add to list 
    dic_students[x[1]] =  Student(id = x[1],name = x[2], date_of_birth = x[3] , class_study = x[4]) # add to dictionary 
    
# print(students[2]) # test print students in dictionary
# success 

#for x in dic_students: # show the list of dic # success
#    print(x)   # show the key of the value
    
def Search_By_Id(x):
    for i in dic_students : 
        if x == i : 
            print(dic_students[x])
            return 
    print("Not Found Same ID")
    return

def Search_By_Name(x): # success 
    for i in dic_students:
        if x == dic_students[i].name :
            print(dic_students[i])
            return
    print("Not found the same name")
    return

id_to_find = input("Enter ID you want to find = ")
Search_By_Id(id_to_find)
name_to_find = input("Name = ")
Search_By_Name(name_to_find)