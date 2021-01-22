from django.shortcuts import render, HttpResponse, redirect
from .models import Book

# Create your views here.
def homepage(request):
    return render(request, "index.html")

def book(request):
    book_list = Book.objects.all()
    return render(request, "books.html", {"book_list": book_list})

def add_book(request):
    return render(request, "add_book.html")

def add_books(request):
    form = request.POST
    title = form["title"]
    subtitle = form["subtitle"]
    description = form["description"]
    price = form["price"]
    genre = form["genre"]
    author = form["author"]
    year = form["year"]
    book1 = Book(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book1.save()
    return redirect(book)

def delete_book(request, id):
    book1 = Book.objects.get(id=id)
    book1.delete()
    return redirect(book)

def fav_book(request, id):
    book1 = Book.objects.get(id=id)
    book1.is_favorite = True
    book1.save()
    return redirect(book)

def unfav_book(request, id):
    book1 = Book.objects.get(id=id)
    book1.is_favorite = False
    book1.save()
    return redirect(book)