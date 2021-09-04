import pandas as pd
from sklearn import preprocessing
from sklearn import *
import numpy as np
from io import StringIO
import redis

df = pd.read_excel('titanicpart.xls','titanicpart', index_col=None)

encoder = preprocessing.LabelEncoder()
df.sex = encoder.fit_transform(df.sex)
df.embarked = encoder.fit_transform(df.embarked)

mean = df.groupby(["pclass","sex"])[["survived","age","sibsp","parch","fare","embarked"]].mean()

X = df.drop(['survived'],axis=1).values
Y = df['survived'].values
X_train = X[:-3]
X_test  = X[-3:]
Y_train = Y[:-3]
Y_test  = Y[-3:]

cl_tree = tree.DecisionTreeClassifier(max_depth=10, random_state=0)
cl_tree.fit(X_train, Y_train)

the_tree = cl_tree
#print(the_tree)
t_nodes = the_tree.tree_.node_count
#print(t_nodes)
t_left = the_tree.tree_.children_left
#print(t_left)
t_right = the_tree.tree_.children_right
#print(t_right)
t_feature = the_tree.tree_.feature
t_threshold = the_tree.tree_.threshold
t_value = the_tree.tree_.value
feature_names = df.drop(['survived'], axis=1).columns.values

forrest_cmd = StringIO()
forrest_cmd.write("ML.FOREST.ADD titanic:tree 0 ")

stack = [ (0, ".") ]

while len(stack) > 0:
    node_id, path = stack.pop()

    if (t_left[node_id] != t_right[node_id]):
        stack.append((t_right[node_id], path + "r"))
        stack.append((t_left[node_id], path + "l"))
        cmd = "{} NUMERIC {} {} ".format(path, feature_names[t_feature[node_id]], t_threshold[node_id])
        forrest_cmd.write(cmd)
    else:
        cmd = "{} LEAF {} ".format(path, np.argmax(t_value[node_id]))
        forrest_cmd.write(cmd)

r = redis.StrictRedis('localhost', 6379)
r.execute_command(forrest_cmd.getvalue())

s_pred = cl_tree.predict(X_test)

r_pred = np.full(len(X_test), -1, dtype=int)
for i, x in enumerate(X_test):
    cmd = "ML.FOREST.RUN titanic:tree "

    for j, x_val in enumerate(x):
        cmd += "{}:{},".format(feature_names[j], x_val)

    cmd = cmd[:-1]
    r_pred[i] = int(r.execute_command(cmd))

print("Y:test", Y_test)
print("r:pred", r_pred)
print("s:pred", s_pred)
