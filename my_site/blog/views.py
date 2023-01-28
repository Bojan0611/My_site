from django.shortcuts import render
from django.http import HttpResponse


def starting_page(request):
    return HttpResponse("It works!")

def posts(request):
    pass

def post_details(request):
    pass