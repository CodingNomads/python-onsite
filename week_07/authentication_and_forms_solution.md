# User Authentication through Django Forms

In this project we will practice to use Django Forms for the common functionality of signing up and logging in users of an app, as well as using custom forms to gather other types of user input and do something with it.

* Set up a new Django project and a new Django App
* Register the relevant URLs etc.
* Using default Forms for User management, create a `/frontpage` with the possibility for new users to sign up and for existing users to log in to the app
* Add a `/profile` page that displays the authenticated user's name when they are signed in, and allows them to sign out again (remember to name the associated view `signout()` to avoid conflicts with Django built-in functions!)

# Challenges

- Extend the App with a custom Django Form that takes in an API key, to allow an API call to the [New York Times top stories API](https://developer.nytimes.com/top_stories_v2.json#/README)
- Extend the default User Model and the `UserCreation` form so that new users add their NYT API keys already when signing up
- Create a new Form that allows users to select from the different available `<sections>` of the NYT top-stories API to display the different results
- Display and filter the results in your `/profile` site to show the title, abstract, and a clickable URL of the related NYT story


# Resources

* [Forms API Django docs](https://docs.djangoproject.com/en/2.1/ref/forms/api/)
* [MDN Docs on Forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
* [Project code on GitHub](https://github.com/martin-martin/django-simple-auth)
* [Extending the Django User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone)
* [NYT top stories API docs](https://developer.nytimes.com/top_stories_v2.json#/README)

# Code Snippets

**`views.py`**

This code creates the main logic of our sign-up and sign-in process. We are using Django provided functions as well as standard Django Forms to make authentication relatively simple.


```python
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def frontpage(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        if request.method == 'POST':
            # determine through the name="" in our HTML form which of the
            # two possible POST requests were sent, and react accordingly
            if 'signupform' in request.POST:
                signupform = UserCreationForm(data=request.POST)
                signinform = AuthenticationForm()

                if signupform.is_valid():
                    username = signupform.cleaned_data['username']
                    password = signupform.cleaned_data['password1']
                    signupform.save()
                    # make life easier for our new users and sign them in
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/')

            # this part happens when the signinform was submitted
            else:
                signinform = AuthenticationForm(data=request.POST)
                signupform = UserCreationForm()

                if signinform.is_valid():
                    login(request, signinform.get_user())
                    return redirect('/')

        # if it's not a POST request, render both forms empty
        else:
            signupform = UserCreationForm()
            signinform = AuthenticationForm()

    return render(request, 'frontpage.html', {'signupform': signupform,
                                              'signinform': signinform})


@login_required
def signout(request):
    logout(request)
    return redirect('/')
```


**`frontpage.html`**

In the related `.html` page, we're implementing the HTML form. The `action="."` redirects to the view it was called by and re-renders it - however now using a different HTTP method (POST), that we defined in `method="post"`.

Through this, the execution takes a different path in the associated view function (see above).

```python
{% extends 'base.html' %}

{% block content %}

<div>
  <h2>Sign in</h2>

  <form action="." method="post">
    {% csrf_token %}

    {{ signinform.as_p }}

    <input type="submit" value="Sign in" name="signinform">
  </form>
</div>

<div>
  <h3>Don't have an account yet?</h3>

  <form action="." method="post">
    {% csrf_token %}

    {{ signupform.as_p }}

    <input type="submit" value="Sign up" name="signupform">
  </form>
</div>

{% endblock %}
```
