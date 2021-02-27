from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout


def logout(request):
    # print('Logging out {}'.format(request.user))
    auth_logout(request)
    return redirect('home')
