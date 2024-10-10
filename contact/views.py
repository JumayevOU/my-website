from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMe
from about.models import About
from collection.models import Collection  

def contactView(request):
    about = About.objects.all()
    contactme = ContactMe.objects.all()
    collections = Collection.objects.all().order_by('-id')[:6]  
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'abouts': about,
        'form': form,
        'me': contactme,
        'collections': collections, 
    }
    return render(request, 'contact.html', context)
