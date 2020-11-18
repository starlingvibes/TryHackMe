from django.shortcuts import render


def index(request):
    render(request, "index.html")
