from django.shortcuts import render, redirect
from .models import ToDo, Comment

# Create your views here.
def home(request):
    todos = ToDo.objects.all().order_by('duedate')
    return render(request, 'home.html', {'todos':todos})

def new(request):
    print(request.POST)
    if request.method == "POST":
        new_todo = ToDo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            duedate = request.POST['duedate'],
        )
        return redirect('detail', list_pk=new_todo.pk)
    else:
        return render(request, 'new.html')

def detail(request, list_pk):
    todo = ToDo.objects.get(pk=list_pk)

    if request.method == "POST":
        Comment.objects.create(
            todo = todo,
            content = request.POST['content']
        )
        return redirect('detail', list_pk)

    return render(request, 'detail.html', {'todo':todo})

def edit(request, list_pk):
    todo = ToDo.objects.get(pk=list_pk)
    if request.method =="POST":
        ToDo.objects.filter(pk=list_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            duedate = request.POST['duedate'],
        )
        return redirect('detail', list_pk)
    return render(request, 'edit.html', {'todo':todo})

def delete(request, list_pk):
    todo = ToDo.objects.get(pk=list_pk)
    todo.delete()
    return redirect('home')

def delete_comment(request, list_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', list_pk)
