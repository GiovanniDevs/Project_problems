from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProblemList.as_view(), name='home'),
]
