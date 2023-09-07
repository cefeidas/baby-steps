from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import SearchForm, UserSearchForm


# views.py

def fetch_books(request, search_form):
    query = ""
    books_list = Book.objects.all().order_by('title')

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

    paginator = Paginator(books_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return {
        'form': search_form,
        'books': page_obj,
        'query': query
    }

def fetch_users(request, search_form):
    query = ""
    user_list = User.objects.all()

    if search_form.is_valid():
        query = search_form.cleaned_data['query']
        field = search_form.cleaned_data['field']

        if field == 'user_name':
            user_list = user_list.filter(username__icontains=query)
        elif field == 'reviews':
            # Assuming you have a related field 'reviews' on CustomUser
            user_list = user_list.filter(reviews__icontains=query)
        elif field == 'ratings':
            # Assuming you have a related field 'ratings' on CustomUser
            user_list = user_list.filter(ratings__icontains=query)
            
    paginator = Paginator(user_list, 25)  # 25 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return {
        'form': search_form,
        'users': page_obj,
        'query': query
    }

def users(request):
    form = UserSearchForm(request.GET)
    user_list = User.objects.all()
    
    field = request.GET.get('field')
    query = request.GET.get('query')

    if field and query:
        kwargs = {f"{field}__icontains": query}
        user_list = User.objects.filter(Q(**kwargs))
    
    paginator = Paginator(user_list, 5)
    page = request.GET.get('page')
    users = paginator.get_page(page)

    return render(request, 'users.html', {'form': form, 'users': users})

def library_home(request):
    print("Library Home View Triggered")
    form = SearchForm(request.GET or None)
    context = fetch_books(request, form)
    return render(request, 'library/library_home.html', context)

def catalog(request):
    form = SearchForm(request.GET or None)
    context = fetch_books(request, form)
    return render(request, 'library/catalog.html', context)

def users(request):
    form = UserSearchForm(request.GET or None)
    context = fetch_users(request, form)
    return render(request, 'library/users.html', context)


def events(request):
    return render(request, 'library/events.html')


def contact(request):
    return render(request, 'library/contact.html')


def about(request):
    return render(request, 'library/about.html')
