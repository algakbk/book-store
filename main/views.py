from django.shortcuts import render, HttpResponse, redirect
from .models import Book

# Create your views here.

def homepage(request):
    book_list = Book.objects.all()
    return render(request, "index.html", {"book_list": book_list})