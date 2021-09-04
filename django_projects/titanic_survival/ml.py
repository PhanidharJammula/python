import redis

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load out data
boston = load_boston()

# slice the data into train and test sets
x_train = boston.data[:400]
x_test =  boston.data[400:]
y_train = boston.target[:400,]
y_test = boston.target[400:,]

# fit the regression line
lm = LinearRegression()
lm.fit(x_train, y_train)

y_predict = lm.predict(x_test)

coef = lm.coef_
inter = lm.intercept_

for col, c in zip(boston.feature_names, coef):
    print('{colname:7}:t{coef:0.6f}'.format(colname=col,coef=c))
print("Intercept: {inter}".format(inter=inter))



# set the linear regression in Redis
cmd = ["ML.LINREG.SET", "boston_house_price:full"]
cmd.append(str(inter))
cmd.extend([str(c) for c in coef])

r = redis.StrictRedis('localhost', 6379)
r.execute_command(*cmd)
