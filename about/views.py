from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm

# Create your views here.


def about_me(request):
    """
    Renders the About page
    """

    about = About.objects.all().order_by('-updated_date').first()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Contact form sent! "
                "I endeavour to respond within 2 working days.")
            contact_form = ContactForm()
    else:
        contact_form = ContactForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "contact_form": contact_form,
        },
    )
