from django.urls import path
from . import views

app_name = 'likes'

urlpatterns = [
    path('greet/', views.index, name='index'),
    path('result/', views.get_page_data, name='get_page_data'),
]
