import pandas as pd
from sklearn import preprocessing
from sklearn import *
import numpy as np
from StringIO import StringIO
import redis

orig_df = pd.read_excel('titanic3.xls','titanic3',index_col = None)
df = orig_df.drop(["name","body","ticket","body","cabin","home.dest"],axis=1)
df = df.dropna()

encoder = preprocessing.LabelEncoder()
df.sex = encoder.fit_transform(df.sex)
df.embarked = encoder.fit_transform(df.embarked)

mean = df.groupby(["pclass","sex"])[["survived","age","sibsp","parch","fare","embarked"]].mean()

X = df.drop(['survived'],axis=1).values
y = df['survived'].values
print(x.head(10))
