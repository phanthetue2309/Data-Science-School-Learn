import pandas as pd

dataset = pd.read_csv("state.csv")
dataset = dataset.sort_values(by=['Murder.Rate'])
dataset.head() #in ra các bản ghi đầu tiên

## Mean: Giá trị trung bình

rows = dataset.shape[0] #xem số lượng dòng(bang)
mean = 0
for i in range(0, rows):
    mean = mean + dataset.loc[i][2] #chọn hàng i cột 2 (cột tỷ lệ giết người)
mean = mean / rows
print("Mean: ", mean)

## Trimmed Mean: Giá trị trung bình tinh gọn

p = int(rows / 10)
trimmed_mean = 0
for i in range(p, rows - p):
    trimmed_mean = trimmed_mean + dataset.loc[i][2]
trimmed_mean = trimmed_mean / (rows - 2 * p)
print("Trimmed_mean: ", trimmed_mean)

## Weighted Mean: Giá trị trung bình có trọng số

weighted_mean = 0
sum_weigth = 0
for i in range(0, rows):
    weighted_mean = weighted_mean + dataset.loc[i][2] * dataset.loc[i][1] #dân số nhân tỉ lệ giết người
    sum_weigth = sum_weigth + dataset.loc[i][1] #tổng dân số các bang
weighted_mean = weighted_mean / sum_weigth
print("Weighted_mean: ", weighted_mean)


## Meadian: Trung vị

median = dataset.loc[int(rows / 2)][2]# chọn giá trị ở giữa danh sách
print("Median: ", median)

## Standar deviation: Độ lệch chuẩn

import math

# mean population
mean_population = 0
for i in range(0, rows):
    mean_population = mean_population + dataset.loc[i][1]
mean_population = mean_population / rows #tính giá trị trung bình dân số mỗi bang

sd = 0
for i in range(0, rows):
    sd = sd + (mean_population - dataset.loc[i][1]) ** 2 #tính phương sai
sd = math.sqrt(sd / (rows - 1))
print("Standar deviation: ", sd)

## MAD

mad = 0
for i in range(0, rows):
    mad = mad + abs(mean_population - dataset.loc[i][1])
mad = mad / (rows - 1)# tính trung vị của độ lệch tuyệt đối so với trung vị
print("MAD: ", mad)

## Biểu đồ tần suất

# sap xep
df_population = dataset.sort_values(by=['Population'])
df_population = df_population.reset_index(drop=True) #đặt lại chỉ mục
df_population.head(6) #in ra 6 bản ghi đầu tiên

# chia thành 10 khoảng
n = 10
d = (df_population.loc[rows - 1][1] - df_population.loc[0][1]) / n - 1

first_index = 0
first_bound = df_population.loc[first_index][1]
last_bound = first_bound + d

# colums
BinNumber = []
BinRange = []
Count = []
State = []
for i in range(0, n):
    arr = []
    if i == n - 1:
        last_bound = df_population.loc[rows - 1][1] #nếu i là số cuối thì cho nó là last_bound
    for j in range(first_index, rows):
        if df_population.loc[j][1] > last_bound:
            break
        else:
            arr.append(df_population.loc[j][3])
    # add row
    BinNumber.append(i) # i sẽ được thêm vào phần tử cuối của mảng
    BinRange.append(str(first_bound) + '-' + str(last_bound))#thêm phần tử vào vị trí cuối của mảng
    Count.append(len(arr)) # tăng count
    State.append(arr)# thêm 1 bang vào vị trí cuối

    first_bound = last_bound + 1 #first_bound tăng thêm 1 khoảng last_bound
    last_bound = first_bound + d #tăng last_bound lên 1 khoảng d
    first_index = j # first_index sẽ là j( với j là hàng đầu tiên trong khoảng tiếp theo)

dataframe = pd.DataFrame(columns=['BinNumber', 'BinRange', 'Count', 'State'])

dataframe['BinNumber'] = BinNumber
dataframe['BinRange'] = BinRange
dataframe['Count'] = Count
dataframe['State'] = State
dataframe.head(10)

print(dataframe)