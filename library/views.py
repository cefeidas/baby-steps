from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book
from django.db.models import Q


def library_home(request):
    
    return render(request, 'library/library_home.html')


def catalog(request):
    query = request.GET.get('query', '')
    field = request.GET.get('field', 'title')
    books = Book.objects.all()
    if query:
        filter_args = {f'{field}__icontains': query}
        books = books.filter(**filter_args)

    context = {
        'books': books,
        'query': query,
    }
    return render(request, 'library/catalog.html', context)



def events(request):
    return render(request, 'library/events.html')


def contact(request):
    return render(request, 'library/contact.html')


def about(request):
    return render(request, 'library/about.html')
