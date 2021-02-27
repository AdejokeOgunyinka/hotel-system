from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout as auth_logout, login, authenticate
from django.contrib.auth.decorators import login_required
from db.models.user import User
from ..forms.signup_form import SignupForm


def signup(request):
    context = {}
    form = SignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            # print(user)
            login(request,user)
            return redirect('dashboard')
    context['form']=form
    return render(request, 'sign_up.html', context)
