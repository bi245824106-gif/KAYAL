import pandas as pd
df=pd.read_csv("C:\\Users\\STUDENT\\AppData\\Local\\Programs\\Python\\Python313\\AN06.csv")
df=df.drop_duplicates()
df=df.dropna()
df.to_csv("newdetails.csv")
print('done')
print(df)
df['revenue']=df['revenue'].replace(r'[^0-9]','',regex=True).astype(int)
df['total workers']=df['workers']+df['previous_workers']
df.to_csv("newdetails.csv",index=False)
print("done")
print(df)
