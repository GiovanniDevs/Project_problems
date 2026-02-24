# Responsiveness

**Larger screens**

![alt text](static/testing/PC.png)

**Tablets**

![alt text](static/testing/pad.png)

**Smartphones**

![alt text](static/testing/phone.png)

# Browser Compatibility

![alt text](static/testing/compat.png)
![alt text](static/testing/browsers.png)

<br>

# Bug Fixing

### 1 - During a particular deployment, heroku would successfully deploy but the app would show an error on launching:

![heroku app launch error](static/testing/validation/error1.png)

#### Troubleshoting:

Using Heroku CLI I was able to get to the actual errors and successfully retrieve valuable information.
<img src="static/testing/CLI.png" width="700">

The problem was a compatibility issue between:

- Gunicorn 20.1.0
- setuptools 82+
- Python 3.12

#### Solution:

Update gunicorn to >= 22.0.0

### 2 - After implementing search functionality in the view, a pagination issue occurred when logged-in users wouldn't see authored Problems waiting for approval

#### Troubleshoting:

Wrong filter logic was the root cause.
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

The solution was for filtering based on the current user:

```Python
if user.is_authenticated:
    qs = qs.filter(
        Q(status='public') | Q(author=user)
    )
else:
    qs = qs.filter(status='public')
```

The solution was for filtering based on the current user:

<img src="static/testing/search.png" width="500">

<br>
<br>

# Lighthouse results

All major Lighthouse advisories about Performance and SEO were implemented.

![alt text](static/testing/lighth.png)

<br>

# Code validation

## HTML

Validation performed via

<details>
<summary>Templates Screenshots</summary>

### Home page:

![alt text](static/testing/validation/home.png)

### Problems List:

![alt text](static/testing/validation/index.png)

### Problem Details:

![alt text](static/testing/validation/pro_details.png)

### Submit page:

![alt text](static/testing/validation/submit.png)

### About page:

![alt text](static/testing/validation/about.png)

### Signup page:

![alt text](static/testing/validation/signup.png)

### Login:

![alt text](static/testing/validation/login.png)

### Logout:

![alt text](static/testing/validation/logout.png)

</details>

## CSS

Validation performed via

<details>
<summary>CSS Screenshot</summary>

![alt text](static/testing/validation/css.png)

</details>

## Phyton

Validation performed via

<details>
<summary>Python Screenshots</summary>

### Problem App

#### Models

![alt text](static/testing/validation/models.png)

#### Views

![alt text](static/testing/validation/views.png)

#### Forms

![alt text](static/testing/validation/forms.png)

#### Urls

![alt text](static/testing/validation/urls.png)

---

### About App

#### Models

![alt text](static/testing/validation/aboutmodels.png)

#### Views

![alt text](static/testing/validation/aboutviews.png)

#### Forms

![alt text](static/testing/validation/aboutforms.png)

</details>

## JavaScript

Validation performed via

<details>
<summary>Python Screenshots:</summary>

### Edit and Delete buttons functionality

![alt text](static/testing/validation/buttons.png)

### GSAP Animations

![alt text](static/testing/validation/gsapanimation.png)

</details>

<br>

# User Stories Testing

| User Story                                                                                             | Test                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| As a visitor, I want to browse public problems so I can explore what issues people are facing          | Problem index page can be easily accessed by all users, display all relevant details.                                                                                                      |
| As a registered user, I want to create a new problem post so I can share workplace frustrations        | If logged in, users can submit a validated form as a new problem with all relevant field, draft is saved for admin publication                                                             |
| As a registered user, I want to edit my own problems so I can update or correct information            | Clicking on edit button performs expected operation on pre-populated form.                                                                                                                 |
| As a registered user, I want to delete my own problems so I can remove content I no longer want public | Clicking on delete button performs expected operation on pre-populated form.                                                                                                               |
| As a visitor, I want to view detailed information about a problem so I can understand it fully         | Problem detail page shows all relevant information about the selected problem and related takes.                                                                                           |
| As a registered user, I want to add my take on a problem so I can share my experience                  | Take form performs as expected in manual testing.                                                                                                                                          |
| As a visitor, I want to register and log in so I can participate in the platform                       | Clicking on Register, Login and Logout (and Submit when not logged in) correctly prompts the relevant template. Templates perform as expected and user is created,logged in or logged out. |
| As a visitor, I want to contact the site administrators so I can ask questions or report issues.       | Form was filled and submitted following correct validation. Admin can read the submitted form from the admin panel                                                                         |
| As a visitor, I want to search and filter problems so I can find relevant issues                       | Typed a few keywords in the search bar, which returned the correct filtered queryset                                                                                                       |
| As a visitor, I want to view an About page so I can understand the platform's mission                  | Clicking on about page renders the correct template and return the correct site information.                                                                                               |
| As an admin, I want to moderate problems and takes so I can maintain platform quality                  | Visiting admin panel "status" of problems and take can be adjusted to public or draft.                                                                                                     |

<br>

# Features

### Manual Testing

| Feature              | Action                                | Effect                                                                                                |
| -------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Navbar               | clicking on each link                 | direct to correct template                                                                            |
| Search Bar           | Search for "customer"                 | returns correct filtered list                                                                         |
| Pagination           | Click on PREV or NEXT                 | Show the next or previous set of entries                                                              |
| Take validation      | Try submitting invalid/valid form     | Shows error/confirm message at the top, retain current form content and shows help text (if invalid). |
| Take edit/delete     | Click on edit/delete buttons          | Perform expected operations and includes user messages, modals, draft status, author ownership check  |
| Problem form choices | Click on each dropdown menu available | Shows expected model fields                                                                           |
| Problem validation   | Try submitting invalid/valid form     | Shows error/confirm message at the top, retain current form content and shows help text (if invalid). |
| Problem edit/delete  | Click on edit/delete buttons          | Perform expected operations and includes user messages, modals, draft status, author ownership check  |
| User creation        | Click on register                     | Form successfully creates a new user on submission                                                    |
| User login           | Click on login                        | Form successfully logs in existing users                                                              |
| User logout          | Click on logout                       | Form successfully logs out existing users                                                             |
| Contact form usage   | Submit contact form                   | Form successfully submits and admin can access content via admin panel                                |
