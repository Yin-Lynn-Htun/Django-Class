from django.urls import path
from . import views


urlpatterns = [
    path('', views.index ), # challenges/
    path('<day>/' , views.daily),
]
