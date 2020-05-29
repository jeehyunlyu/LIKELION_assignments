from django.shortcuts import render, redirect
from .models import ToDo, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    todos = ToDo.objects.all().order_by('duedate')
    return render(request, 'home.html', {'todos':todos})

@login_required(login_url="/registration/login")
def new(request):
    print(request.POST)
    if request.method == "POST":
        new_todo = ToDo.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            duedate = request.POST['duedate'],
            author = request.user,
        )
        return redirect('detail', list_pk=new_todo.pk)
    else:
        return render(request, 'new.html')

def detail(request, list_pk):
    todo = ToDo.objects.get(pk=list_pk)

    if request.method == "POST":
        Comment.objects.create(
            todo = todo,
            content = request.POST['content'],
            author = request.user,
        )
        return redirect('detail', list_pk)

    return render(request, 'detail.html', { 'todo': todo })

def edit(request, list_pk):
    todo = ToDo.objects.get(pk=list_pk)
    if request.method =="POST":
        ToDo.objects.filter(pk=list_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            duedate = request.POST['duedate'],
            author = request.user,
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

def mypage(request):
    todos = ToDo.objects.all().order_by('duedate')
    comment = Comment.objects.all()
    return render(request, 'mypage.html', {'todos': todos, 'comment': comment})

def signup(request):
    if request.method == "POST":
        found_user = User.objects.get(username=request.POST['username'])
        if found_user is not None:
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html', { 'error' : error })

        new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(
            request, 
            new_user, 
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('home')

    return render(request, 'registration/signup.html')

def login(request):
    if request.method == "POST":
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', { "error": error })

        auth.login(
            request, 
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect(request.GET.get('next', '/'))
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect("home")