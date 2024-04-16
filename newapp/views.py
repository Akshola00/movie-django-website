from django.shortcuts import render
from .models import movies
from django.core.paginator import Paginator
# Create your views here.

def movie_list(request):
    movies_objects = movies.objects.all()
    paginator = Paginator(movies_objects, 3)
    page = request.GET.get('page')
    movies_objects = paginator.get_page(page)
    context = {
        'movies_objects':movies_objects
    }
    return render(request, 'newapp/movie_list.html', context)