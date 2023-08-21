from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book
from django.db.models import Q
from .forms import SearchForm

def library_home(request):
    
    return render(request, 'library/library_home.html')


def catalog(request):
    form = SearchForm(request.GET or None)
    query = ""
    books_list = Book.objects.all()

    if form.is_valid():
        query = form.cleaned_data['query']
        field = form.cleaned_data['field']

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

    paginator = Paginator(books_list, 5) # Show 5 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form, # Add form to context for rendering in the template
        'books': page_obj,
        'query': query
    }
    return render(request, 'library/catalog.html', context)



def events(request):
    return render(request, 'library/events.html')


def contact(request):
    return render(request, 'library/contact.html')


def about(request):
    return render(request, 'library/about.html')
