""""Module imports"""
from django.shortcuts import render

# Create your views here.
def get_todo_list(request):
    """View rendering todo list html"""
    return render(request, "todo/todo_list.html")
