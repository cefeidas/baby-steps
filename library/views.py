from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Book, Review
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import SearchForm, UserSearchForm, ReviewForm, SelectBookForm


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
        
        # Handle undefined fields to prevent 404 errors
        try:
            if field == 'username':  # Changed 'user_name' to 'username' to match Django's built-in User model
                user_list = user_list.filter(username__icontains=query)
                
            elif field == 'reviews':
                # Insert your query logic here for 'reviews'
                pass  # Remove this line once you insert your logic
                
            elif field == 'ratings':
                # Insert your query logic here for 'ratings'
                pass  # Remove this line once you insert your logic
                
            else:
                user_list = User.objects.none()  # Returns an empty queryset if the field is not recognized
        except Exception as e:
            print(f"An error occurred: {e}")  # Log the error for debugging
            user_list = User.objects.none()  # Returns an empty queryset if an exception occurs

    paginator = Paginator(user_list, 25)  # Show 25 users per page
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

# views.py

# ... other imports ...

@login_required
def add_review(request):
    user = request.user
    selected_book = None

    if 'selected_book' in request.session:
        book_id = request.session['selected_book']
        selected_book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'select_book':
            select_book_form = SelectBookForm(request.POST)
            if select_book_form.is_valid():
                selected_book = select_book_form.cleaned_data['title']
                request.session['selected_book'] = selected_book.id
                
        elif form_type == 'add_review':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = user
                review.book = selected_book
                review.save()
                del request.session['selected_book']
                return redirect('reviews')

    else:
        select_book_form = SelectBookForm()
        review_form = ReviewForm()

    return render(request, 'library/add_review.html', {
        'select_book_form': select_book_form,
        'review_form': review_form,
        'selected_book': selected_book
    })





def reviews(request):
    return render(request, 'library/reviews.html')

