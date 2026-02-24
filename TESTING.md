![alt text](static/testing/pc.png)
![alt text](static/testing/pad.png)
![alt text](static/testing/phone.png)
![alt text](static/testing/compat.png)
![alt text](static/testing/browsers.png)

# Bug Fixing

big problem deploying with horoku initially as apparently it would fail unless switched to

gunicorn==22.0.0 instead of 20

fixed using heroku CLI

<img src="static/testing/CLI.png" width="500">

After implementing search functionality in the view, a pagination issue occurred when logged-in users wouldn't see authored Problems waiting for approval
<img src="static/testing/search.png" width="500">

favicon is not served if not in static folder
correct link

<link rel="icon" type="image/x-icon" href="{% static 'favicon.ico' %}">

# lighthouse

![alt text](static/testing/lighth.png)

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

### CSS

![alt text](static/testing/validation/css.png)

</details>

## Phyton

Validation performed via

<details>
<summary>Python Screenshots:</summary>

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
![alt text](static/testing/validation/aboutforms.png)
![alt text](static/testing/validation/aboutmodels.png)
![alt text](static/testing/validation/aboutviews.png)
