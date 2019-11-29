from django.shortcuts import render

posts = [
    {
        'author':'DavidD',
        'title':'Random 1',
        'content': 'First bug',
        'date_posted': 'December 24, 2030',
        
    },
     {
        'author':'Vasile BOss',
        'title':'Random 2',
        'content': 'Second bug',
        'date_posted': 'December 25, 2030',
        
    },
    {
        'author':'Vasile BOss',
        'title':'Random 2',
        'content': 'Second bug',
        'date_posted': 'December 25, 2030',
        
    },
    {
        'author':'Vasile BOss',
        'title':'Random 2',
        'content': 'Second bug',
        'date_posted': 'December 25, 2030',
        
    },
    {
        'author':'Vasile BOss',
        'title':'Random 2',
        'content': 'Second bug',
        'date_posted': 'December 25, 2030',
        
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/bugs.html', context, {'title': 'Bugs'})

def bugs(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/bugs.html', context, {'title': 'Bugs'})

def contact(request):
    return render(request, 'blog/contact.html')
