class Murder : 
    def __init__(self,state,population, murderRate,abbreviation):
        self.state = state
        self.population = population
        self.murderRate = murderRate
        self.abbreviation = abbreviation
    def __repr__(self):
        return str(dict({
            "state": self.state,
            "population" : self.population,
            "murderRate" : self.murderRate,
            "abbreviation": self.abbreviation,
        }))

murder = []
dic_murder = dict()

f = open("state.csv", 'r',encoding="utf-8")
listoflines = f.readlines()
i = 0
count = 0

for line in listoflines:
    if i == 0 : # skip line header
        i = 1
        continue
    count += 1 
    x = line.split(",")
    murder.append(Murder(state = x[0], population = float(x[1]), 
        murderRate= float(x[2]), abbreviation=x[3])) # add to list 
    dic_murder[count] =  Murder(state = x[0], population = float(x[1]), 
        murderRate= float(x[2]), abbreviation=x[3]) 
        # count ở đây hiểu như gán khóa key cho dic_murder
        
sum_mean = sum_weigth_mean = sum_weight = sum_mean_absolute_deviation = sum_MAD = 0 

murderRate = population = []

for murder in dic_murder:
    sum_mean += dic_murder[murder].murderRate
    sum_weigth_mean += dic_murder[murder].murderRate * dic_murder[murder].population
    sum_weight += dic_murder[murder].population
    murderRate.append(dic_murder[murder].murderRate)
    population.append(dic_murder[murder].population)

murderRate.sort()   # sắp xếp lại danh sách

murder2 = murderRate[5:45]
sum_murder2 = sum(murder2)

mean = sum_mean / count
print("mean = ", mean)
print("weight_mean =", sum_weigth_mean / sum_weight)
print("trimmed = " ,sum_murder2 / (count - 10)) 
print("median = ", murderRate[int(count / 2)])

for murder in dic_murder:
    sum_mean_absolute_deviation += abs(dic_murder[murder].murderRate - mean)

mean_absolute_deviation = sum_mean_absolute_deviation / count

print("mean_absolute_deviation = ", mean_absolute_deviation)
print("MAD Murderate = ", sum_mean_absolute_deviation / mean)

Q1 = (murderRate[12] + murderRate[13]) / 2
Q3 = (murderRate[37] + murderRate[38]) / 2
print("IQR Murderate = ", Q3 - Q1)

mean_population = sum(population) / len(population)

for i in range(0,len(population)):
    sum_MAD += abs(population[i] - mean_population)
print("MAD Population = ",sum_MAD / len(population))

population.sort()

Q1 = (population[12] + population[13]) / 2
Q3 = (population[37] + population[38]) / 2
print("IQR Population = ", Q3 - Q1)