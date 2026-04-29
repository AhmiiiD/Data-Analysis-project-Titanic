import pandas as pd
import numpy as np

def prepare_data(path):
    df=pd.read_csv(path).dropna(how='all')
    print("The Number of Duplicated Rows = ",df.duplicated().sum())
    print("The Number of Raws in the data = ",len(df))
    df['Survived']=df['Survived'].replace({0:'Died',1:'Survived'})
    df['Pclass']=df["Pclass"].replace({1:"First Class",2:'Second Class',3:"Third Class"})
    df['Age']=df['Age'].astype('float32')
    df['Survived']=df['Survived'].astype('category')
    df['Pclass']=df['Pclass'].astype('category')
    df['Embarked']=df['Embarked'].astype('category')
    df['Sex']=df['Sex'].astype('category')
    df['SibSp']=df['SibSp'].astype('Int8')
    df['Parch']=df['Parch'].astype('Int8')
    # remove the high cardinality columns
    df.drop(['Name','PassengerId','Ticket','Cabin'],axis=1,inplace=True)
    return df
