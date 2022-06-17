from django.shortcuts import render

from django.http import HttpResponse , JsonResponse

def index_view (request):
    return HttpResponse('<h1>homw page </h1>')


def about_view(request):
    return HttpResponse('hi my name is jeff')

def contact_view(request):
    return HttpResponse('this is my telegram')

