from django.shortcuts import render
from .models import About
from collection.models import Collection

def aboutView(request):
    about = About.objects.all()
    collections = Collection.objects.order_by('-pk')[:6] 
    context = {
        'abouts': about,
        'collections': collections,
    }
    return render(request, 'about.html', context)
