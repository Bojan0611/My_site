from django.shortcuts import render
from django.http import HttpResponseRedirect


def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_details(request):
    pass