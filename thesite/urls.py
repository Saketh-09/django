from django.urls import path
from . import views

urlpatterns = [
    path('', views.signupPage1, name='signup1'),
    path('<int:id>', views.signupPage2, name='signup2'),
    path('login', views.login_user, name='login'),
    path('homme', views.home, name='homme'),
    path('logout', views.logout_user, name='logout'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('superlogin', views.login_superuser, name='superlogin')
]
