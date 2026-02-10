from django.shortcuts import render
from django.views import generic
from .models import Problem

# Create your views here.


class ProblemList(generic.ListView):
    queryset = Problem.objects.all()
    template_name = "problems/problems_list.html"
