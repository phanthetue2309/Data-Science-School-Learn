import pandas as pd
import numpy as np
from prettytable import PrettyTable

data_excel = pd.read_excel('Book1.xlsx')

stt=[]
id_card = []
name=[]
date=[]
class_study=[]

rows = data_excel.shape[0]

df = pd.DataFrame(data_excel)
# return a dictionary 
# print(df.blocks) # không còn hỗ trợ

for i in range(0,rows):
    id_card.append(data_excel.loc[i][1])
    name.append(data_excel.loc[i][2])
    date.append(data_excel.loc[i][3])
    class_study.append(data_excel.loc[i][4])