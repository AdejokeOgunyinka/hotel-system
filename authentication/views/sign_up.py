from django.shortcuts import render, redirect
from django.contrib.auth import login
from db.models.user import User
from ..forms.signup_form import SignupForm


def signup(request):
    context = {}
    form = SignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    context['form']=form
    return render(request, 'sign_up.html', context)
