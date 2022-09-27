from django.contrib.auth.models import User


class EmailBackend(object):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print('hiiiioi')
        try:
            user = User.objects.filter(email=username).first()
        except User.DoesNotExist:
            return None
        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            print(User.objects.get(pk=user_id))
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
