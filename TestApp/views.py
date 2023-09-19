from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def supp(request):
    return render(request, "supp.html")

def page2(request):
    return render(request, "page2.html")

# Create your views here.
