from django.shortcuts import render
from .models import Book


def library_home(request):
    
    return render(request, 'library/library_home.html')


def catalog(request):
    Books  = Book.objects.all()
    context = {
        'books' : Books
    }
    return render(request, 'library/catalog.html', context)


def events(request):
    return render(request, 'library/events.html')


def contact(request):
    return render(request, 'library/contact.html')


def about(request):
    return render(request, 'library/about.html')
