from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book
from django.db.models import Q
from .forms import SearchForm

# views.py

def fetch_books(request, search_form):
    query = ""
    books_list = Book.objects.all()

    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        field = search_form.cleaned_data['field']

        if field == 'title':
            books_list = books_list.filter(title__icontains=query)
        elif field == 'writer':
            books_list = books_list.filter(writer__icontains=query)
        elif field == 'genre':
            books_list = books_list.filter(genre__icontains=query)
        elif field == 'editorial':
            books_list = books_list.filter(editorial__icontains=query)
        elif field == 'isbn':
            books_list = books_list.filter(isbn__icontains=query)

    paginator = Paginator(books_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return {
        'form': search_form,
        'books': page_obj,
        'query': query
    }

def library_home(request):
    form = SearchForm(request.GET or None)
    context = fetch_books(request, form)
    return render(request, 'library/library_home.html', context)

def catalog(request):
    form = SearchForm(request.GET or None)
    context = fetch_books(request, form)
    return render(request, 'library/catalog.html', context)




def events(request):
    return render(request, 'library/events.html')


def contact(request):
    return render(request, 'library/contact.html')


def about(request):
    return render(request, 'library/about.html')
