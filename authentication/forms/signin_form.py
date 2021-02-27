from django import forms as django_form
from db.models.user import User


class SigninForm(django_form.ModelForm):
    password = django_form.CharField(widget=django_form.PasswordInput(), required=True)
    confirm_password = django_form.CharField(widget=django_form.PasswordInput(), required=True)
    
    class Meta:
        model = User
        fields = ["email", "password"]
