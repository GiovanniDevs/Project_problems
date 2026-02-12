from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Problem
from .forms import TakeForm

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
    takes = problem.takes.all().order_by("-created_date")
    takes_count = problem.takes.filter(status='public').count()

    if request.method == "POST":
        take_form = TakeForm(data=request.POST)
        if take_form.is_valid():
            take = take_form.save(commit=False)
            take.author = request.user
            take.problem = problem
            take.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Take submitted and awaiting approval'
            )
            take_form = TakeForm()  # only reset AFTER successful save
    else:
        take_form = TakeForm()

    return render(
        request,
        "problems/problem_detail.html",
        {
            "problem": problem,
            "takes": takes,
            "takes_count": takes_count,
            "take_form": take_form,
        },
    )
