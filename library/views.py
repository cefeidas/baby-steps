from django.shortcuts import render

# Create your views here.
def library_project(request):
    return render(request, 'library/library_home.html')
