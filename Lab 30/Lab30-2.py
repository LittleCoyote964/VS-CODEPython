import pandas as pd

mydict = [['Tom', 35, 'Plumber'],
           ['Adam', 41, 'Pilot'],
           ['Chris', 23, 'Mechanic'],
           ['Jose', 28, 'Retail Manager'],
           ['John', 17, 'Store Member']]

column_names = ['NAME', 'AGE', 'JOB']

df = pd.DataFrame(mydict, columns = column_names)
print(df)

df.to_csv('Employment.csv', header = False, index = False)
#remove rows with people who are less than 20 years old.
print('\nRemoving employees that are the below the age of 20: \n')
print(df[df.AGE < 20])

dropped = df[df['AGE'] < 20].index
df = df.drop(dropped)
print('\n')
print(df)
df.to_csv('UpdatedEmployment.csv', header = False, index = False)