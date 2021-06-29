import pandas as pd
import numpy as np
data = {'name':['david','gru','kid','ram','ilya'],
'age': [24, 10, 3, np.nan, 79],
'bad health':['False', 'True', 'Excellent', 'Excellent', 'bad']
}
print(data.keys())
df = pd.DataFrame(data, columns=data.keys())
print(df)

print(df.count())
print(df.count(axis=1))

df.sort_values(by='name')
print(df)
print(df.sort_values(by=['name','age'])) #doesn't incorporate second variable and sorts only
#on the basis of first row/column name passed to it. If inplace = True, updates the original df
#but returns none. Returns a new df for inplace = False.














