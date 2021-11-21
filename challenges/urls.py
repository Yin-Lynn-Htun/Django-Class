from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='index'), # challenges/
    path('<int:day>/' , views.daily_by_number, name="daily_by_number"),
    path('<str:day>/', views.daily, name="daily")
]
