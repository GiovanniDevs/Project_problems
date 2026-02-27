# Responsiveness

**Larger Screens**

![Screenshot of larger screen layout](static/testing/PC.png)

**Tablets**

![Screenshot of tablet layout](static/testing/pad.png)

**Smartphones**

![Screenshot of smartphone layout](static/testing/phone.png)

# Browser Compatibility

![Browser compatibility matrix](static/testing/compat.png)
![Supported browsers](static/testing/browsers.png)

<br>

# Bug Fixing

### 1 - During a particular deployment, Heroku would successfully deploy but the app would show an error on launching:

![Heroku app launch error](static/testing/validation/error1.png)

#### Troubleshooting:

Using the Heroku CLI, I was able to get to the actual errors and successfully retrieved valuable information.
<img src="static/testing/CLI.png" width="700">

The problem was a compatibility issue among:

- Gunicorn 20.1.0
- setuptools >= 82
- Python 3.12

#### Solution:

Update Gunicorn to version 22.0.0 or higher.

### 2 - After implementing search functionality in the view, a pagination issue occurred when logged-in users wouldn't see authored Problems waiting for approval.

#### Troubleshooting:

The root cause was incorrect filter logic.
Original view:

```Python
def get_queryset(self):
    qs = Problem.objects.all()
    q = self.request.GET.get('q', '').strip()
    user = self.request.user

    if q:
        qs = qs.filter(
            Q(title__icontains=q) |
            Q(industry__icontains=q) |
            Q(description__icontains=q) |
            Q(author__username__icontains=q)
        )
    return qs
```

#### Solution:

The solution was to filter based on the current user:

```Python
if user.is_authenticated:
    qs = qs.filter(
        Q(status='public') | Q(author=user)
    )
else:
    qs = qs.filter(status='public')
```

<br>
<br>

# Lighthouse Results

All major Lighthouse advisories regarding performance and SEO were addressed.

![Lighthouse results screenshot](static/testing/lighth.png)

<br>

# Code Validation

## HTML

Validation performed using https://validator.w3.org/

<details>
<summary>Templates Screenshots</summary>

### Home page:

![Home page HTML validation screenshot](static/testing/validation/home.png)

### Problems List:

![Problems list HTML validation screenshot](static/testing/validation/index.png)

### Problem Details:

![Problem details HTML validation screenshot](static/testing/validation/pro_details.png)

### Submit page:

![Submit page HTML validation screenshot](static/testing/validation/submit.png)

### About page:

![About page HTML validation screenshot](static/testing/validation/about.png)

### Signup page:

![Signup page HTML validation screenshot](static/testing/validation/signup.png)

### Login:

![Login page HTML validation screenshot](static/testing/validation/login.png)

### Logout:

![Logout page HTML validation screenshot](static/testing/validation/logout.png)

</details>

## CSS

Validation performed using https://jigsaw.w3.org/css-validator/

<details>
<summary>CSS Screenshot</summary>

![CSS validation screenshot](static/testing/validation/css.png)

</details>

## Python

Validation performed using https://pep8ci.herokuapp.com/

<details>
<summary>Python Screenshots</summary>

### Problem App

#### Models

![Problem app models validation screenshot](static/testing/validation/models.png)

#### Views

![Problem app views validation screenshot](static/testing/validation/views.png)

#### Forms

![Problem app forms validation screenshot](static/testing/validation/forms.png)

#### Urls

![Problem app urls validation screenshot](static/testing/validation/urls.png)

---

### About App

#### Models

![About app models validation screenshot](static/testing/validation/aboutmodels.png)

#### Views

![About app views validation screenshot](static/testing/validation/aboutviews.png)

#### Forms

![About app forms validation screenshot](static/testing/validation/aboutforms.png)

</details>

## JavaScript

Validation performed using https://jshint.com/

<details>
<summary>JavaScript Screenshots:</summary>

### Edit and Delete Buttons Functionality

![Edit and delete buttons validation screenshot](static/testing/validation/buttons.png)

### GSAP Animations

![GSAP animation validation screenshot](static/testing/validation/gsapanimation.png)

</details>

<br>

# User Stories Testing

| User Story                                                                                             | Test                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| As a visitor, I want to browse public problems so I can explore what issues people are facing          | The problem index page can be easily accessed by all users and displays all relevant details.                                                                                                  |
| As a registered user, I want to create a new problem post so I can share workplace issues              | If logged in, users can submit a validated form as a new problem with all relevant fields; the draft is saved for admin publication.                                                           |
| As a registered user, I want to edit my own problems so I can update or correct information            | Clicking the edit button performs the expected operation on a pre-populated form.                                                                                                              |
| As a registered user, I want to delete my own problems so I can remove content I no longer want public | Clicking the delete button performs the expected operation on a pre-populated form.                                                                                                            |
| As a visitor, I want to view detailed information about a problem so I can understand it fully         | The problem detail page shows all relevant information about the selected problem and related takes.                                                                                           |
| As a registered user, I want to add my take on a problem so I can share my experience                  | The take form performs as expected during manual testing.                                                                                                                                      |
| As a visitor, I want to register and log in so I can participate in the platform                       | Clicking Register, Login, and Logout (and Submit when not logged in) correctly prompts the relevant template. Templates perform as expected and the user is created, logged in, or logged out. |
| As a visitor, I want to contact the site administrators so I can ask questions or report issues.       | The form was filled and submitted following correct validation. The admin can read the submitted form from the admin panel.                                                                    |
| As a visitor, I want to search and filter problems so I can find relevant issues                       | Typing keywords in the search bar returns the correct filtered queryset.                                                                                                                       |
| As a visitor, I want to view an About page so I can understand the platform's mission                  | Clicking on the About page renders the correct template and returns the correct site information.                                                                                              |
| As an admin, I want to moderate problems and takes so I can maintain platform quality                  | In the admin panel, the status of problems and takes can be adjusted to public or draft.                                                                                                       |

<br>

# Features

### Manual Testing

| Feature              | Action                                  | Effect                                                                                                              |
| -------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Navbar               | Click each link                         | Directs to the correct template.                                                                                    |
| Search Bar           | Search for "customer"                   | Returns the correct filtered list.                                                                                  |
| Pagination           | Click PREV or NEXT                      | Shows the next or previous set of entries.                                                                          |
| Take validation      | Try submitting an invalid or valid form | Shows an error or confirmation message at the top, retains current form content, and displays help text if invalid. |
| Take edit/delete     | Click the edit or delete buttons        | Performs expected operations and includes user messages, modals, draft status, and author ownership checks.         |
| Problem form choices | Click each available dropdown menu      | Displays expected model fields.                                                                                     |
| Problem validation   | Try submitting an invalid or valid form | Shows an error or confirmation message at the top, retains current form content, and displays help text if invalid. |
| Problem edit/delete  | Click the edit or delete buttons        | Performs expected operations and includes user messages, modals, draft status, and author ownership checks.         |
| User Creation        | Click register                          | The form successfully creates a new user upon submission.                                                           |
| User Login           | Click login                             | The form successfully logs in existing users.                                                                       |
| User Logout          | Click logout                            | The form successfully logs out existing users.                                                                      |
| Contact Form Usage   | Submit the contact form                 | The form is successfully submitted and the admin can access the content via the admin panel.                        |
