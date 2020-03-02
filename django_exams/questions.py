intro = """# QUESTIONS TO ANSWER FOR STUDENTS

Split up in groups of two/three and research and answer
common questions related to Django and Web Development.

After 2 hours of research time, you'll present the results
to the rest of the class.

----------------------------------------------------------


"""


question_text = """
What is a `@staticmethod`, what is a `@classmethod`?

What does python's `__init__.py` file do? Why is it used in Django?

What makes an API a REST API?

Explain the concept of HTTP requests and responses.

What are HttpRequest and HttpResponse objects in Django? How do they differ from HTTP requests/responses?

When and how do you cache stuff? What does it mean?

What is Cross Site Request Forgery and how can you prevent it?

What is TDD (Test-driven development)? What's the advantage of using it?

How do HTML forms work? What's their syntax, what are they used for?

What is CSS and what is it used for?

What is a "project" in Django, what are "apps"? Which metaphors related to other programming concepts can you come up with?

What are some Django best practices (in terms of performance, organization of Apps, organization of static and media files, security)?

What are common bugs in Django 2.0/2.1 (and which ones were resolved from earlier versions)?

What is a CSRF token and how does it work?

What is "middleware"

What functionality do the different Middlewares created by `django-admin startproject` provide (high-level explanation)?

What does registering an app in `INSTALLED_APPS` achieve?

What is the suggested folder structure for templates? And why is it like that?

What are the available methods inside of `django.shortcuts`? What processes do they simplify?

What is the class Meta: construct in Django classes (e.g. Models and Serializers)?

What is a Mixin in Django? How is it used?

What are template context processors (in settings file), and why are the default ones (debug, request, auth, messages) included? What are other common ones that people use?

What is `reverse()` about in Django?

What does `ugettextlazy` do? When and where would you use it?

How does testing in Django work?

What is a good way to debug Django apps during production?

How does Django process a HTTP request? What happens inside of `urls.py` and what do `path()` and `include()` do respectively?

What are Django's class based views, and why would you want to use them?

What are Django's `generic` views? Which common ones exist and what can they be used for?

Explain a few of the most common tags in the Django templating language.

How do you create a reusable app in Django?

What happens behind the scenes of the Django ORM?

What is `blank=True, null=True` that you might see in a couple of models?

How does the Django ORM translate to SQL find (or make!) a conversion chart.

How does a database such as MySQL differ from SQLite (standard in Django)?

How do you get a recently saved instance of a ModelForm object? What does `.save()` return?

What are some different ways to delete user-uploaded files when the associated object is deleted?

What happens when you run `python manage.py makemigrations`?

What happens when you run `python manage.py migrate`?

What are `unittest`s and how do they work?

How do you correctly remove one app from a Django project without impacting the data provided by other apps?

What are 5 big companies or projects that use Django?
"""

questions = [q for q in question_text.split('\n') if q != '']

group1 = []
group2 = []
group3 = []

count = 1
for q in questions:
    if count == 1:
        group1.append(q)
        count += 1
    elif count == 2:
        group2.append(q)
        count += 1
    elif count == 3:
        group3.append(q)
        count = 1


# testing...

def equal_spread(g1, g2, g3):
    return len(g1) == len(g2) == len(g3)


def all_questions_assigned_and_not_too_many(g1, g2, g3, original):
    return set(g1 + g2 + g3) == set(original)


def no_question_lost_and_none_duplicated(g1, g2, g3, original):
    return len(g1 + g2 + g3) == len(original)


print("equal spread: ", equal_spread(group1, group2, group3))
print("same content: ", all_questions_assigned_and_not_too_many(group1,
                                                                group2,
                                                                group3,
                                                                questions))
print("same length: ", no_question_lost_and_none_duplicated(group1,
                                                            group2,
                                                            group3,
                                                            questions))

# creating files...

groups = [group1, group2, group3]

counter = 1
for group in groups:
    with open(f'questions_group_{counter}.md', 'w') as fout:
        text = intro + '* ' + '\n\n* '.join(group)
        fout.write(text)
    counter += 1
