from django.contrib import messages
from django.shortcuts import redirect


class RestrictMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *args, **kwargs):
        path = request.path_info.lstrip('/')
        print(path)
        if (not request.user.is_authenticated and request.path != '/'
            and request.path != '/login' and request.path != '/logout'
                and request.path != '/superlogin' and request.path != '/admin/'
                and request.path != '/data'):
            messages.error(
                request, ("Not logged in!, Restricted through middleware"))
            return redirect('/login')
