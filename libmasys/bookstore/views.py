from django.shortcuts import render,redirect

from django.http import HttpResponse


def index(request):
    if (request.method == 'POST'):
        return redirect('admin/login')
    else:
        return render(request,'hijo.html')

def addBook(request):
    return redirect('/admin/bookstore/libro/add/')
