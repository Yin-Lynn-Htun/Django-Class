from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ), # challenges/
    path('<int:day>/' , views.daily_by_number),
    path('<str:day>/', views.daily)
]
