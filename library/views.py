from django.shortcuts import render
from .models import Book
from django.db.models import Q


def library_home(request):
    
    return render(request, 'library/library_home.html')


def catalog(request):
    query = request.GET.get('query', '')
    books = Book.objects.all()

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(genre__icontains=query) |
            Q(editorial__icontains=query) |
            Q(isbn__icontains=query) |
            Q(writer__icontains=query)
        )

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
