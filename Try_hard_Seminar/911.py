import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
df = pd.read_csv('911.csv')

top5zip = df['zip'].value_counts().head(5)    # use method value_counts() it give top 5 highest
print(top5zip)

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
#print(df['Reason'])
df['Reason'].value_counts()

sns.countplot(x='Reason',data=df,palette='viridis')
plt.show()

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)  #time la doi so vao va o day pandas doi so vao la time cung cap ham sai dc
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)  # method of pandas 

# start to draw day of the week here
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)


# To relocate the legend
sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

# end draw 
sns.countplot(x='Month',data=df,hue='Reason',palette='viridis') # x have to same in df such as df["Month"]
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
# end draw month

byMonth = df.groupby('Month').count()
byMonth.head()
byMonth['twp'].plot()
