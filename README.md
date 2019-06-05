# Starting a Webpage in Django

**Prerequisites:**

* Pyenv
* Python
* Virtualenv
* Django
* Text editor of choice

1. Start your virtual environment

1. Install Django with: pip install Django

1. Then, cd into the folder you want your test project to be stored in, or create one yourself

1. Create your Django project using: django-admin startproject hello_world_project

1. cd into hello_world_project

1. Start your app using:
python manage.py startapp my_app

1. cd into my_app

1. Using the text editor of choice, add the following to the views.py file:

```from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World!')
```

Next, cd out of the my_app folder and open the urls.py file and change it so it looks like the following:

```from django.contrib import admin
from django.urls import path
    # imported views
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # configured the url
    path('',views.index, name="homepage")
]
```

## Running Webpage

1. Use: python manage.py runserver

1. Navigate to your browser and enter the address that popped up in the terminal

Use CTRL + c in the terminal to exit

**For more information, use:** [this link](https://djangocentral.com/create-a-hello-world-django-application)
