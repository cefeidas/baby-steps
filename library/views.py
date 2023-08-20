from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book
from django.db.models import Q


def library_home(request):
    
    return render(request, 'library/library_home.html')


from django.core.paginator import Paginator
from .models import Book

def catalog(request):
    query = request.GET.get('query', '')
    field = request.GET.get('field', 'title')
    books_list = Book.objects.all()
    if query:
        filter_args = {f'{field}__icontains': query}
        books_list = books_list.filter(**filter_args)

    paginator = Paginator(books_list, 5) # Show 5 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'books': page_obj,
        'query': query,
    }
    return render(request, 'library/catalog.html', context)




def events(request):
    return render(request, 'library/events.html')


def contact(request):
    return render(request, 'library/contact.html')


def about(request):
    return render(request, 'library/about.html')
