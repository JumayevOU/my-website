from django.shortcuts import render, redirect
from about.models import About
from collection.models import Collection
from .models import Blog, Category, Tag
from .forms import CommentForm


def indexView(request):
    about = About.objects.all()
    collections = Collection.objects.order_by('-id')[:6]
    context = {
        'abouts': about,
        'collections': collections,
    }
    return render(request, 'index.html', context)


def blogView(request):
    about = About.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    blog = Blog.objects.all().order_by('-id')
    collections = Collection.objects.order_by('-pk')[:6]
    context = {
        'abouts': about,
        'categories': category,
        'tags': tag,
        'blogs': blog,
        'collections': collections,
    }
    return render(request, 'blog.html', context)


def detailView(request, pk):
    blog1 = Blog.objects.all().order_by('-id')
    about = About.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()

    
    blog = Blog.objects.get(id=pk)
    collections = Collection.objects.order_by('-pk')[:6]
    comments = blog.comment.all()

    form = CommentForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.blog = blog
        com.save()
        return redirect('.')

    context = {
        'blog1': blog1,
        'abouts': about,
        'blogs': blog,
        'collections': collections,
        'categories': category,
        'tags': tag,
        'comments': comments,  
        'form': form,
    }
    return render(request, 'single.html', context)


def commentView(request, pk):
    about = About.objects.all()
    blog = Blog.objects.get(id=pk)
    collections = Collection.objects.order_by('-pk')[:6]
    context = {
        'abouts': about,
        'blogs': blog,
        'collections': collections,
    }

    return render(request, 'single.html', context)

