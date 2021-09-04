from user.views import Train, Predict
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('train/', Train.as_view(), name="train"),
    path('Predict/', Predict.as_view(), name="predict"),
]
