from django.shortcuts import render, HttpResponse, redirect
from .models import Book

# Create your views here.

def homepage(request):
    book_list = Book.objects.all()
    return render(request, "index.html", {"book_list": book_list})

def add_book(request):
    return render(request, "add_book.html")

def add_books(request):
    form = request.POST
    book_title = form["book_title"]
    subtitle = form["subtitle"]
    description = form["description"]
    price = form["price"]
    genre = form["genre"]
    author = form["author"]
    year = form["year"]

    book1 = Book(book_title=book_title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book1.save()
    return redirect(homepage)