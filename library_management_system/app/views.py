from django.shortcuts import render , HttpResponse , redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from .models import Book

def book(request):
    books = Book.objects.all() 
    return render(request, 'book.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id= id)
    return render(request, 'book_detail.html', {'book': book})

def home(request):
   return render(request,'home.html')


def acc(request):
    return render(request,'acc.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!= pass2:
            return HttpResponse("Incorrect input")
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            return redirect('loginpage')
    return render(request,"index.html")
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        pas = request.POST.get('password')
        user=authenticate(request,username=username,password=pas)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Incorrect Input")
    return render(request, 'log.html')