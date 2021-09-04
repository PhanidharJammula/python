from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
#import pandas as pd

import redis

boston = load_boston()
boston_RM = boston.data[:,5]
boston_PRICE = boston.target



#slice the data into train and test datasets
x_train = boston_RM[:400].reshape(-1,1)
x_test = boston_RM[:400].reshape(-1,1)
y_train = boston.target[:400]
y_test = boston.target[400:]

lm= LinearRegression()
lm.fit(x_train, y_train)

co = lm.coef_
int = lm.intercept_

# print("Coef: {coef}, Intercept:{int}".format(coef=coef,int=int))
#
# r = redis.StrictRedis('localhost', 6379)
# r.execute_command("ML.LINREG.SET", "boston_house_price:rm-only",  "-35.2609481316348", "9.40550212",)
#
# redis_predict= []
#
# for x in x_test:
#     y = r.execute_command("ML.LINREG.PREDICT", "boston_house_price:rm-only", x[0])
#     redis_predict.append(float(y))
# y_predict = lm.predict(x_test)
# print(y_predict)


#WE are using multiple LinearRegression now
for col, c in zip(boston.feature_names, co):
    print('{colname:7}:t{coef:0.6f}'.format(colname=col,coef=c))
    print("Intrecept: {inter}".format(inter=inter))

cmd= ["ML.LINREG.SET", "boston_house_price:full"]
cmd.append(str(inter))
cmd.extend([str(c) for c in coef])

r=redis.StrictRedis('localhost', 6379)
r.execute_command(*cmd)
