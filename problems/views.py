from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Problem, Take
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


def take_edit(request, slug, take_id):
    # view to edit Takes

    if request.method == "POST":
        queryset = Problem.objects.filter(status='public')
        problem = get_object_or_404(queryset, slug=slug)
        take = get_object_or_404(Take, pk=take_id)
        take_form = TakeForm(data=request.POST, instance=take)

        if take_form.is_valid() and take.author == request.user:
            take = take_form.save(commit=False)
            take.problem = problem
            take.approved = False
            take.save()
            messages.add_message(request, messages.SUCCESS, 'Take Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating take!')

    return HttpResponseRedirect(reverse('problem_detail', args=[slug]))


def take_delete(request, slug, take_id):
    """
    view to delete take
    """
    queryset = Problem.objects.filter(status='public')
    problem = get_object_or_404(queryset, slug=slug)
    take = get_object_or_404(Take, pk=take_id)

    if take.author == request.user:
        take.delete()
        messages.add_message(request, messages.SUCCESS, 'Take deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own Takes!')

    return HttpResponseRedirect(reverse('problem_detail', args=[slug]))
