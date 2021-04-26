import pandas
import numpy as np
from prettytable import PrettyTable


excel_data_df = pandas.read_excel('CheckIN.xlsx', skiprows = 6,sheet_name='Data In',na_filter=False)
# na_filter dùng để xóa dữ liệu rỗng
person = ["NGUYEN VAN A", "NGUYEN VAN B","NGUYEN VAN C","NGUYEN VAN D",
          "NGUYEN VAN E", "NGUYEN VAN F","NGUYEN VAN G",]
dict_person = {0:"NGUYEN VAN A" , 1:"NGUYEN VAN B", 2:"NGUYEN VAN C", 3:"NGUYEN VAN D", 
4:"NGUYEN VAN E", 5:"NGUYEN VAN F", 6:"NGUYEN VAN G"}
df = pandas.DataFrame(excel_data_df) 
# print whole sheet data
#print(excel_data_df)
result = df.loc[:, ["TIME", "CH1", "CH2"]] 
# print(result)
# data = result.iloc[0]
# print(data)
# print(data[0] , data[1], data[2])

check_in = []
list_time = [" "] * 10 
print(list_time)
for i in range(0,len(result)):
    data = result.iloc[i]
    date_time = str(data[0]).split(" ")
    date = date_time[0]
    if (date == "NaT" ):
        break
    time = str(data[0]).split(" ")[1]
    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])
    seconds = time.split(":")[2]
    seconds = int(seconds.split(".")[0])
    total_time = hour*3600 + minute*60 + seconds
    if data[1] in person and data[1] not in check_in:
        check_in.append(data[1])
        for key in dict_person:
            if data[1] == dict_person[key]:
                if int(total_time) > 51361 : 
                    list_time[key] = "LATE"
                else :
                    list_time[key] ="ON TIME"
        

z = PrettyTable(['STT','Name', 'Appear', "LATE / ON TIME"])
n = 0 
for i in person:
    if i in check_in:
        z.add_row([n+1,i,"YES",list_time[n]])
    if i not in check_in:
         z.add_row([n+1,i,"NO",list_time[n]])

    n += 1
    
print(z)