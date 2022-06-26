from django.shortcuts import render

posts = [
    {
        'author': 'MarkH',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 26 2022'
    },
    {
        'author': 'JaneDoe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 28 2022'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')