from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from db.models.user import User
from ..forms.signin_form import SigninForm


def signin(request):
    context = {}
    form =SigninForm(request.POST or None)
    if request.method == "POST":
        email_address = form.data['email']
        password = form.data['password']
        user = User.objects.get(email=email_address)
        password_correct = (password == user.password)

        if user is not None and password_correct:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse('Please enter a valid email and password combination.')
    context['form']=form
    return render(request, 'sign_in.html', context)
