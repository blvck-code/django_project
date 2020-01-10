from django.shortcuts import render

posts = [
    {
        'author': 'KidRyan',
        'title': 'Post One',
        'content': 'First Content Post',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Diana Sydney',
        'title': 'Post Two',
        'content': 'Second Content Post',
        'date_posted': 'August 28, 2019'
    }
]

def home(request):
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})