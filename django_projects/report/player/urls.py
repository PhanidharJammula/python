from player.views import Activity
from django.urls import path
from . import views

app_name = 'player'

urlpatterns = [
    path('greet/', views.index, name='index'),
    path('activity/',Activity.as_view(),name='Activity'),
]
