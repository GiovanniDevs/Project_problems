from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProblemList.as_view(), name='home'),
    path('<slug:slug>/', views.problem_detail, name='problem_detail'),
    path('<slug:slug>/edit_take/<int:take_id>',
         views.take_edit, name='take_edit'),
    path('<slug:slug>/delete_take/<int:take_id>',
         views.take_delete, name='take_delete'),
]
