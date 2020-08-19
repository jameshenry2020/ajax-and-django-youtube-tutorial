from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def postlist_view(request):
    return render(request, "posts/index.html")


def post_fetch(request):
    limit=request.GET.get('limit')
    start=request.GET.get('start')
    posts=BlogPost.objects.all()[int(start):int(start) + int(limit)]
    context={
        "post_list":posts
    }
    return render(request, 'posts/result.html', context)


