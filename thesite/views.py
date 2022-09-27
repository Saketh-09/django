from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.forms import modelformset_factory, formset_factory

from shoppingitems.models import ShopingItem
from .models import Signup, UserDetails
from .forms import UserDetailsForm, SignupForm, LoginForm, RegistrationForm
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .decorator import is_superuser
from rest_framework import viewsets
from shoppingitems.serializers import ShoppinItemSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from shoppingitems import serializers

# Create your views here.


def signupPage1(request):
    if request.user.is_authenticated:
        return redirect(reverse('homme'))
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        else:
            return HttpResponse('Username or Password requirements are not met')
    else:
        form = RegistrationForm()
        context['form'] = form
        return render(request, 'signup.html', context)


def signupPage2(request, id):
    context = {}
    UserDetailsFormset = formset_factory(
        UserDetailsForm)
    formset = UserDetailsFormset(request.POST or None)
    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                a = UserDetails(userID=id, name=form.cleaned_data['name'],
                                phone=form.cleaned_data['phone'], place=form.cleaned_data['place'])
                a.save()
                break
            return HttpResponseRedirect(reverse('home', args=[id]))
    context['formset'] = formset
    return render(request, 'signup2.html', context)


@is_superuser
def home(request):
    context = {}
    curr_user = request.user
    context['name'] = curr_user.username
    context['email'] = curr_user.email
    return render(request, 'home.html', context)


def login_user(request):
    context = {}
    details = {}
    form = LoginForm(request.POST or None)
    context['form'] = form
    if request.user.is_authenticated:
        return redirect(reverse('homme'))
    if request.method == 'POST':
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request,
                                username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('homme'))
            else:
                return HttpResponse('Invalid email or password')
        else:
            return HttpResponse('Invalid email or password')
    else:
        return render(request, 'login.html', context)


def changepassword(request):
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = PasswordChangeForm(user=request.user)
        context['form'] = form
        return render(request, 'changepassword.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, ("Logged out!"))
    return redirect(reverse('login'))


@is_superuser
def login_superuser(request):
    context = {}
    form = LoginForm(request.POST or None)
    context['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,
                                username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'home.html', {'username': username, 'email': email})
            else:
                return HttpResponse('Invalid email or password')
        else:
            return HttpResponse('Invalid email or password')
    else:
        return render(request, 'login.html', context)


@api_view(['GET', 'POST'])
def api_list(request):
    if request.method == 'GET':
        queryset = ShopingItem.objects.all()
        serializers = ShoppinItemSerializers(queryset, many=True)
        return Response(serializers.data)

    if request.method == 'POST':
        queryset = ShopingItem.objects.all()
        serializers = ShoppinItemSerializers(queryset, many=True)
        return Response(serializers.data)
