from django.shortcuts import render
from django.http import HttpResponse


'''def index(request):
    #name = request.GET.get("name") or "world!"
    name = "Hamad"
    return render(request,"bookmodule/index.html", {"name": name})'''


def index2(request, val1 = 0):
    return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookid):
    #assume these book in a database
    book1 = {'id':123, 'title': 'Continuous Delivery','author':'J. Humble and D.Farley'}
    book2 = {'id':456, 'title': 'Secrets of Revers Engineering', 'author':'E. Eilam'}
    book3 = {'id':789, 'title': 'Calculus', 'author':'Hamad. M Alsowayyan'}
    book4 = {'id':789, 'title': 'Calculus', 'author':'Hamad. M Alsowayyan'}
    
    if book1['id'] == bookid:
         targetBook = book1

    if book2['id'] == bookid:
        targetBook= book2
    
    if book3['id'] == bookid:
        targetBook= book3
    context = {'book':targetBook}   #book is a var name accesible by template
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request,'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def text(request):
    return render(request, 'bookmodule/text.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')
