from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProblemList.as_view(), name='home'),
    path('<slug:slug>/', views.problem_detail, name='problem_detail'),
]
