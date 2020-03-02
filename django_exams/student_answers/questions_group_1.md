# QUESTIONS TO ANSWER FOR STUDENTS

Split up in groups of two/three and research and answer
common questions related to Django and Web Development.

After 2 hours of research time, you'll present the results
to the rest of the class.

----------------------------------------------------------


* What is a `@staticmethod`, what is a `@classmethod`?

    With classmethods, the class of the object instance is implicitly passed as the first argument instead of self.

    With staticmethods, neither self (the object instance) nor  cls (the class) is implicitly passed as the first argument. They behave like plain functions except that you can call them from an instance or the class.

    https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod?rq=1

* Explain the concept of HTTP requests and responses.

    HTTP is an internet protocol that handles exchange of information between a client and a server. Using methods such as GET, POST, PATCh.

* What is Cross Site Request Forgery and how can you prevent it?

    Cross-site request forgery, also known as one-click attack or session riding and abbreviated as CSRF (sometimes pronounced sea-surf[1]) or XSRF, is a type of malicious exploit of a website where unauthorized commands are transmitted from a user that the web application trusts.
https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)

* What is CSS and what is it used for?

    Cascading Style Sheet is used to customize HTML page elements by manipulating size, colors, fonts, motions, etc. It is part of the view of the MVC or template of MTV. The power of CSS is you can set one file and cascade it across many pages.

    Cascading Style Sheet is used to customize web page formats. HTML elements by manipulating its definitions

* What are common bugs in Django 2.0/2.1 (and which ones were resolved from earlier versions)?

2.0.7
Fixed admin changelist crash when using a query expression without asc() or desc() in the page’s ordering (#29428).
Fixed __regex and __iregex lookups with MySQL 8 (#29451).
https://code.djangoproject.com/query?status=closed

* What functionality do the different Middlewares created by `django-admin startproject` provide (high-level explanation)?
https://docs.djangoproject.com/en/2.1/ref/middleware/
THe order matters.
Created a folder directory for your project.
Creates manage.py and inner site directory with urls, settings, etc.


'django.middleware.security.SecurityMiddleware',
The django.middleware.security.SecurityMiddleware provides several security enhancements to the request/response cycle. Each one can be independently enabled or disabled with a setting.

    'django.contrib.sessions.middleware.SessionMiddleware',
Session Enables session support.
    'django.middleware.common.CommonMiddleware',
Common - Performs URL re-writing, sets contentlength, forbids access to  DISALLOWED_USER_AGENTS
    'django.middleware.csrf.CsrfViewMiddleware',
CsrfViews - Adds protection against Cross Site Request Forgeries

    'django.contrib.auth.middleware.AuthenticationMiddleware',
Adds the user attribute, representing the currently-logged-in user, to every incoming HttpRequest object
    'django.contrib.messages.middleware.MessageMiddleware',
Enables cookie- and session-based message support.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
Simple clickjacking protection via the X-Frame-Options header.












* What are the available methods inside of `django.shortcuts`? What processes do they simplify?
https://docs.djangoproject.com/en/2.1/_modules/django/shortcuts/
render - Return a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
redirect - Return an HttpResponseRedirect to the appropriate URL for the arguments
    passed.

    get_object_or_404 - Use get() to return an object, or raise a Http404 exception if the object
    does not exist.
* What are template context processors (in settings file), and why are the default ones (debug, request, auth, messages) included? What are other common ones that people use?
context_processors is a list of dotted Python paths to callables that are used to populate the context when a template is rendered with a request. These callables take a request object as their argument and return a dict of items to be merged into the context.
https://docs.djangoproject.com/en/2.1/ref/templates/api/

* How does testing in Django work?
THere is a tests.py file in every app. You can write classes for different functionality and sample scenarios that you want to test against the expected result. You can run these tests in the command line.
https://docs.djangoproject.com/en/2.1/intro/tutorial05/

* What are Django's class based views, and why would you want to use them?
They are used to simplify your views and not have to re-write the same code. You can build one class and have another one inherit. You can use generic views from Django.
https://docs.djangoproject.com/en/2.1/topics/class-based-views/

* How do you create a reusable app in Django?

* How does the Django ORM translate to SQL find (or make!) a conversion chart.

* What are some different ways to delete user-uploaded files when the associated object is deleted?

Store in the DB, make a foreign key to associated object and make it cascade on delete.

* What are `unittest`s and how do they work?

The unittest unit testing framework was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.
https://docs.python.org/2/library/unittest.html

