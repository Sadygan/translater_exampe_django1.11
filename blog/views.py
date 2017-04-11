from django.shortcuts import render
from django.template import Context
from .models import Post


def index(request):
    return render(request, "index.html")


def about(request):
    qs = Post.objects.all()
    print("-----")
    print(qs.first().name)
    context = ({"name": qs[0].name })
    return render(request, "about.html", context)
