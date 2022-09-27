from dataclasses import fields
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import ShoppingItemForm
from django.forms import formset_factory
from .models import ShopingItem
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import ShoppinItemSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse
# Create your views here.


def create_view(request):
    context = {}

    form = ShoppingItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list_view'))
    context["form"] = form

    return render(request, "create_view.html", context)


def detail_view(request, id):
    context = {}

    context["data"] = ShopingItem.objects.get(id=id)

    return render(request, "detail_view.html", context)


def list_view(request):
    context = {}

    context["dataset"] = ShopingItem.objects.all()
    return render(request, "list_view.html", context)


def update_view(request, id):
    context = {}

    obj = get_object_or_404(ShopingItem, id=id)
    form = ShoppingItemForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('detail_view', args=[id]))
        # return HttpResponseRedirect("/"+id)

    context['form'] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):

    obj = get_object_or_404(ShopingItem, id=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(reverse('list_view'))

    return render(request, 'delete_view.html')


@csrf_exempt
@api_view(['GET', 'POST'])
def shopping_list(request):
    if request.method == 'GET':
        items = ShopingItem.objects.all()
        serializer = ShoppinItemSerializers(items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShoppinItemSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET', 'POST'])
def shopping_detail(request, pk):
    try:
        item = ShopingItem.objects.get(pk=pk)
    except:

        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ShoppinItemSerializers(item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShoppinItemSerializers(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
