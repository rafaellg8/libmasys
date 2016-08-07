from django.shortcuts import render,redirect

from django.http import HttpResponse
from .forms import SimpleSearch,Search


def index(request):
    if (request.method == 'POST'):
        return redirect('admin/login')
    else:
        return render(request,'hijo.html')

def addBook(request):
    return redirect('/admin/bookstore/libro/add/')

def search(request):
    if (request.method == 'POST'):
        return render(request,'result.html',{'searchString': request.POST['searchParam']})
    else:
        return redirect('/')

def Search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Search(request.POST)
        # check whether it's valid:
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            return render(request,'result.html', {'author': author,'title': title})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
