from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np
import redis
iris = load_iris()
x_train = [ x for (i, x) in enumerate(iris.data) if i%10 !=0 ]
x_test = [x for (i, x) in enumerate(iris.data) if i%10 == 0]
y_train = [ y for (i, y) in enumerate(iris.target) if i%10 != 0 ]
y_test = [ y for (i, y) in enumerate(iris.target) if i%10 == 0 ]
# print(x_train)
logr = LogisticRegression()
logr.fit(x_train, y_train)
y_pred = logr.predict(x_test)
r = redis.StrictRedis('localhost', 6379)
for i in range(3):
    r.execute_command("ML.LOGREG.SET", "iris-predictor:{}".format(i), logr.intercept_[i], *logr.coef_[i])


# Run predictions in Redis
r_pred = np.full(len(x_test), -1, dtype=int)

for i, obs in enumerate(x_test):
     probs = np.zeros(3)
     for j in range(3):
         probs[j] = float(r.execute_command("ML.LOGREG.PREDICT", "iris-predictor:{}".format(j), *obs))
     r_pred[i] = probs.argmax()

# Compare results as numerical vector
print("y_test = {}".format(np.array(y_test)))
print("y_pred = {}".format(y_pred))
print("r_pred = {}".format(r_pred))
