from django.shortcuts import render
from . models import Todo
# Create your views here.
def index(request):
    tasks = Todo.objects.all()
    context = {'tasks':tasks}
    return render (request, "todo/index.html", context)