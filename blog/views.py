from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'blog/bugs.html')

def bugs(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/bugs.html', context, {'title': 'Bugs'})

def all_bugs(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/all_bugs.html', context, {'title': 'Bugs'})

def contact(request):
    return render(request, 'blog/contact.html')
