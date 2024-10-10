from django.shortcuts import render
from about.models import About
from collection.models import Collection  

def serviceView(request):
    about = About.objects.all()  
    collections = Collection.objects.all().order_by('-id')[:6] 
    context = {
        'abouts': about,
        'collections': collections,  
    }
    return render(request, 'services.html', context)
