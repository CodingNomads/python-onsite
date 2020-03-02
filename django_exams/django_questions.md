# QUESTIONS TO ANSWER FOR STUDENTS

We'll split up in groups of two in order to research and answer some
common questions related to Django and Web Development.

After an hour of research time, we'll present the results to the rest
of the class.



## General Python

- What is a `@staticmethod`, what is a `@classmethod`?

- What does python's `__init__.py` file do? Why is it used in Django?



## General Web Development

- What makes an API a REST API?

- Explain the concept of HTTP requests and responses.

- What are HttpRequest and HttpResponse objects in Django? How do they differ from HTTP requests/responses?

- When and how do you cache stuff? What does it mean?

- What is Cross Site Request Forgery and how can you prevent it?

- What is TDD (Test-driven development)? What's the advantage of using it?

- How do HTML forms work? What's their syntax, what are they used for?

- What is CSS and what is it used for?



## General Django

- What is a "project" in Django, what are "apps"? Which metaphors related to other programming concepts can you come up with?

- What are some Django best practices (in terms of performance, organization of Apps, organization of static and media files, security)?

- What are common bugs in Django 2.0/2.1 (and which ones were resolved from earlier versions)?

- What is a CSRF token and how does it work?

- What is "middleware"

- What functionality do the different Middlewares created by `django-admin startproject` provide (high-level explanation)?

- What does registering an app in `INSTALLED_APPS` achieve?

- What is the suggested folder structure for templates? And why is it like that?

- What are the available methods inside of `django.shortcuts`? What processes do they simplify?

- What is the class Meta: construct in Django classes (e.g. Models and Serializers)?

- What is a Mixin in Django? How is it used?

- What are template context processors (in settings file), and why are the default ones (debug, request, auth, messages) included? What are other common ones that people use?

- What is `reverse()` about in Django?

- What does `ugettextlazy` do? When and where would you use it?

- How does testing in Django work?

- What is a good way to debug Django apps during production?

- How does Django process a HTTP request? What happens inside of `urls.py` and what do `path()` and `include()` do respectively?

- What are Django's class based views, and why would you want to use them?

- What are Django's `generic` views? Which common ones exist and what can they be used for?

- Explain a few of the most common tags in the Django templating language.

- How do you create a reusable app in Django?



## Django ORM and Databases

- What happens behind the scenes of the Django ORM?

- What is `blank=True, null=True` that you might see in a couple of models?

- How does the Django ORM translate to SQL - find (or make!) a conversion chart.

- How does a database such as MySQL differ from SQLite (standard in Django)?

- How do you get a recently saved instance of an object? What does `.save()` return?

- What are some different ways to delete user-uploaded files when the associated object is deleted?

- What happens when you run `python manage.py makemigrations`?

- What happens when you run `python manage.py migrate`?


---



# For later


## Django REST Framework

- What is a 'serializer' in Django (and Django REST framework)? What does it do?
    * https://docs.djangoproject.com/en/2.1/topics/serialization/



## Django on Servers

- What are some common Django security vulnerabilities and how to patch them?

- How does gunicorn know what you're talking about when you say `djangoproject.wsgi`?

- Can you run more than one Django App on a server?

- What steps do you need to make media files work correctly?
    * on the development server `runserver`
    * in production on a remote server

- How can you make a Django app running remotely get automatically restarted when pulling new changes?
    * Check out `gunicorn service.restart`



---



## Tasks and Outlook

- How to make the project template project work with Django 2.x

- Combine the Django API with your wsgi_server project

