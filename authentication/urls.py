from django.urls import path, include
from .views.sign_in import signin
from .views.sign_up import signup 
from .views.dashboard import dashboard
from .views.logout import logout

urlpatterns = [
    path('login', signin, name='login'),
    path('register', signup, name='register'),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard')
]
