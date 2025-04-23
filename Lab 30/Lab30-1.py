import pandas as pd

mydict = [['Tom', '35', 'Plumber'],
           ['Adam', '41', 'Pilot'],
           ['Chris', '23', 'Mechanic'],
           ['Jose', '28', 'Retail Manager'],
           ['John', '17', 'Store Member']]

column_names = ['NAME', 'AGE', 'JOB']

df = pd.DataFrame(mydict, columns = column_names)
print(df)

df.to_csv('Employment.csv', header = False, index = False)