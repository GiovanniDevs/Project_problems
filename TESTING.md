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
