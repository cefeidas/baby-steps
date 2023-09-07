from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Book, Review
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import SearchForm, UserSearchForm, ReviewForm


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

def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.book = book
            review.save()
            # Now the database has been updated.
    else:
        form = ReviewForm()
    return render(request, 'library/add_review.html', {'form': form})



def reviews(request):
    return render(request, 'library/reviews.html')

def select_book_for_review(request):
    if request.method == 'POST':
        form = SelectBookForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['title'].id
            # Redirect to the actual review page for the selected book
            return redirect('library/add_review', book_id=book_id)
    else:
        form = SelectBookForm()
    return render(request, 'library/select_book_for_review.html', {'form': form})
