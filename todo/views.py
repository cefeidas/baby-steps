from django.shortcuts import render

# Create your views here.
def library_project(request):
    return render(request, 'todo/todo_list.html')