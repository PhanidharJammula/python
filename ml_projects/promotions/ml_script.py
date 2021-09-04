import os
import pickle
import numpy as np
import pandas as pd
from sklearn import datasets
from django.conf import settings
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
#from django.shortcuts import render

# Create your views here.
class Train(views.APIView):
    def post(self, request):
        df = pd.read_excel('promotions1.xls')
        #df['promotions']=df['promotions'].astype('category')
        X = df.drop(["PlayerID","promotions"],axis=1)
        y =df['promotions']

        model_name = request.data.pop('model_name')
        print(model_name);
        try:
            #clf = tree.DecisionTreeClassifier(**request.data)
            clf = RandomForestClassifier(**request.data)
            clf.fit(X, y)
        except Exception as err:
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

        path = os.path.join(settings.MODEL_ROOT, model_name)
        with open(path, 'wb') as file:
            pickle.dump(clf, file)
        return Response(status=status.HTTP_200_OK)


class Predict(views.APIView):
    def post(self, request):
        predictions = []
        for entry in request.data:
            model_name = entry.pop('model_name')
            print(model_name);
            path = os.path.join(settings.MODEL_ROOT, model_name)
            with open(path, 'rb') as file:
                model = pickle.load(file)
            try:
                result = model.predict(pd.DataFrame([entry]))
                predictions.append(result[0])

            except Exception as err:
                return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

        return Response(predictions, status=status.HTTP_200_OK)
