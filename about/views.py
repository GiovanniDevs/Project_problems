from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm

# Create your views here.


def about_me(request):
    """
    Render the About page and handle contact form submissions.

    GET: retrieve the most recently updated `About` instance and display an
    empty `ContactForm`.

    POST: validate and save the submitted `ContactForm`, add a success
    message, and reinitialize the form for the response.

    Context:
    - about: latest `About` instance or ``None`` if no records exist
    - contact_form: an instance of `ContactForm` (bound on POST)

    Template: ``about/about.html``
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
