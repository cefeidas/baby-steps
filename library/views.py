from django.shortcuts import render


def library_home(request):
    return render(request, 'library/library_home.html')


def catalog(request):
    return render(request, 'library/catalog.html')


def events(request):
    return render(request, 'library/events.html')


def contact(request):
    return render(request, 'library/contact.html')


def about(request):
    return render(request, 'library/about.html')
