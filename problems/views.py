from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Problem

# Create your views here.


class ProblemList(generic.ListView):
    queryset = Problem.objects.filter(status='public')
    template_name = "problems/index.html"
    paginate_by = 6


def problem_detail(request, slug):
    """
    Display an individual :model:`problems.Problem`.

    **Context**

    ``post``
        An instance of :model:`problems.Problem`.

    **Template:**

    :template:`problems/problem_detail.html`
    """

    queryset = Problem.objects.filter(status='public')
    problem = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "problems/problem_detail.html",
        {"problem": problem},
    )
