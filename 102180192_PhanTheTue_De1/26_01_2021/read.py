class Student : 
    def __init__(self,name,age, score):
        self.name = name
        self.age = age
        self.score = score
    def __repr__(self):
        return str(dict({
            "name": self.name,
            "age" : self.age,
            "score" : self.score,
        }))
   
students = []
dic_students = dict()
while(True):
    line = input("Enter String : ")
    if line == "q" or line =="Q": 
        break
    x = line.split(",")
    students.append(Student(name = x[0], age = int(x[1]) , score = int(x[2]))) # add to list 
#dic_students[x[1]] = Student(name = x[0], age = x[1] , score = x[2])) # add to dictionary 

def sort_name(students):
    return students.name

def sort_age(students):
    return students.age


sort_by_name = sorted(students,key = sort_name)

print("Sort Name :")
print(sort_by_name)

sort_by_age = sorted(students, key = sort_age)
print("Sort Age :")
print(sort_by_age)

