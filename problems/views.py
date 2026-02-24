from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q, Count
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string

from .models import Problem, Take
from .forms import TakeForm, ProblemForm, ProblemSubmitForm

# Create your views here.


class ProblemList(generic.ListView):

    template_name = "problems/index.html"
    paginate_by = 6

    def get_queryset(self):
        qs = Problem.objects.all().annotate(takes_count=Count('takes'))
        q = self.request.GET.get('q', '').strip()
        user = self.request.user

        if user.is_authenticated:
            qs = qs.filter(
                Q(status='public') | Q(author=user)
            )
        else:
            qs = qs.filter(status='public')

        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(industry__icontains=q) |
                Q(description__icontains=q) |
                Q(author__username__icontains=q)
            )
        return qs


def problem_detail(request, slug):
    """
    Display an individual :model:`problems.Problem`.

    **Context**

    ``post``
        An instance of :model:`problems.Problem`.

    **Template:**

    :template:`problems/problem_detail.html`
    """

    queryset = Problem.objects.all()
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
            messages.add_message(
                request, messages.ERROR,
                'Error submitting take. Please check the form and try again.'
            )
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


@login_required
def problem_submit(request):
    if request.method == "POST":
        problem_form = ProblemSubmitForm(data=request.POST)
        if problem_form.is_valid():
            problem = problem_form.save(commit=False)
            problem.author = request.user        # attach logged-in user
            problem.slug = slugify(problem.title)  # auto-generate slug
            while Problem.objects.filter(slug=problem.slug).exists():
                problem.slug = (
                    f"{slugify(problem.title)}-{get_random_string(5)}"
                )
            problem.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Problem submitted and awaiting approval'
            )
            # redirect after success
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error submitting problem. '
                'Please check the form and try again.'
            )
    else:
        problem_form = ProblemSubmitForm()

    return render(
        request,
        "problems/problem_submit.html",
        {"problem_form": problem_form},
    )


@login_required
def problem_edit(request, slug):
    """View to edit a problem - only the author can edit."""
    problem = get_object_or_404(Problem, slug=slug)

    if problem.author != request.user:
        messages.add_message(request, messages.ERROR,
                             'You can only edit your own problems!')
        return HttpResponseRedirect(reverse('problem_detail', args=[slug]))

    if request.method == "POST":
        problem_form = ProblemForm(data=request.POST, instance=problem)
        if problem_form.is_valid():
            problem = problem_form.save(commit=False)
            problem.author = request.user
            # Reset to draft so admin re-approves after edits
            problem.status = 'draft'
            problem.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Problem updated and awaiting re-approval'
            )
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error submitting problem. '
                'Please check the form and try again.'
            )
    else:
        problem_form = ProblemForm(instance=problem)

    return render(
        request,
        "problems/edit_problem.html",
        {
            "problem_form": problem_form,
            "problem": problem
        },
    )


@login_required
def problem_delete(request, slug):
    """View to delete a problem - only the author can delete."""
    problem = get_object_or_404(Problem, slug=slug)

    if problem.author != request.user:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own problems!')
        return HttpResponseRedirect(reverse('problem_detail', args=[slug]))

    if request.method == "POST":
        problem.delete()
        messages.add_message(request, messages.SUCCESS, 'Problem deleted!')
        return HttpResponseRedirect(reverse('home'))

    # If GET, redirect back (deletion should be POST for safety)
    return HttpResponseRedirect(reverse('problem_detail', args=[slug]))
