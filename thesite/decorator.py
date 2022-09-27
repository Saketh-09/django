from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages


def is_superuser(function=None, redirect_url='/'):

    def decorator(view_func):
        def _wrapped(request, *args, **kwargs):
            if request.user.is_superuser:
                messages.info(request, "Welcome..! super User!")
                return view_func(request, *args, **kwargs)
            else:
                messages.info(request, "You are not a super User!")
                return view_func(request, *args, **kwargs)
        return _wrapped

    if function:
        return decorator(function)

    return decorator
