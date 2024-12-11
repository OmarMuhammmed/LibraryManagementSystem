from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.shortcuts import redirect
# Create your views here.


def index(requset):
    if requset.method == 'POST' :
        add_book = AddBookForm(requset.POST,requset.FILES)
        if add_book.is_valid() :
            add_book.save()
            
            add_category = CategoryForm(requset.POST)
            if add_category.is_valid() :
                add_category.save()

    context = {
        'books': Book.objects.all(),
        'category': Category.objects.all(),
        'form' : AddBookForm(),
        'addcat' : CategoryForm(),
        'allbooks':Book.objects.filter(active = True).count(),
        'booksoild':Book.objects.filter(status = 'soild').count(),
        'bookavailable':Book.objects.filter(status = 'available').count(),
        'bookrental':Book.objects.filter(status = 'rental').count(),
    }
    
    return render(requset, 'pages/index.html',context)

def books(requset):
  # search 
  search = Book.objects.all()
  title = None
  if 'search_name' in requset.GET:
    title = requset.GET['search_name']
    if title :
      search = search.filter(title__icontains = title ) # title the name of col in DB


  if requset.method == 'POST' :
    category = CategoryForm(requset.POST)
    if category.is_valid() : #new
      category.save()
  context = {
      'books': search,
      'category': Category.objects.all(),
      'addcat' : CategoryForm(),
  }

  return render(requset, 'pages/books.html',context )

def update(requset,id):
  
  book_id = Book.objects.get(id=id) # get id book 
  if requset.method == 'POST' :
    book_save = AddBookForm(requset.POST, requset.FILES, instance= book_id )
    if book_save.is_valid() :
      book_save.save( )
      return redirect('/') # To back index page 
  else : # this condition frist run 
    book_save = AddBookForm(instance=book_id) 

  context = {
    'upform':book_save, 
    'addcat' : CategoryForm(),
  }

  return render(requset,'pages/update.html',context)

def delete(requset,id):

    book_delete = get_object_or_404(Book, id=id) 
    
    if requset.method =="POST":
        book_delete.delete()
        return redirect('/')

    context={
        'addcat' : CategoryForm(),
    }

    return render(requset,'pages/delete.html',context)