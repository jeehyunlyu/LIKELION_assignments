from django.shortcuts import render, redirect
from .models import Review
import datetime

# Create your views here.

def index(request):
    movies = Review.objects.filter(category="movie")
    dramas = Review.objects.filter(category="drama")
    entertains = Review.objects.filter(category="entertain")
    movies_count = movies.count()
    dramas_count = dramas.count()
    entertains_count = entertains.count()
    return render(request, 'index.html', {'movies_count': movies_count, 'dramas_count': dramas_count, 'entertains_count': entertains_count})

def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_review = Review.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content'],
            time = datetime.datetime.now()
        )
        return redirect('detail', clicked_review_number=new_review.pk)
    else:
        return render(request, 'new.html')

def detail(request, clicked_review_number):
    review = Review.objects.get(pk=clicked_review_number)
    return render(request, 'detail.html', {"review": review})

def movie(request):
    movies = Review.objects.filter(category="movie")
    return render(request, 'movie.html', {"movies": movies})

def drama(request):
    dramas = Review.objects.filter(category="drama")
    return render(request, 'drama.html', {"dramas": dramas})

def entertain(request):
    entertains = Review.objects.filter(category="entertain")
    return render(request, 'entertain.html', {"entertains": entertains})