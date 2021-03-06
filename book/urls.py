"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name="home"),
    path("books/", book, name="books"),
    path("add_book/", add_book, name="add_book"),
    path("add-books/", add_books, name="add-books"),
    path("delete-book/<id>/", delete_book, name="delete-book"),
    path("fav-book/<id>/", fav_book, name="fav-book"),
    path("unfav-book/<id>/", unfav_book, name="unfav-book"),
    path("book-detail/<id>/", booksDetail, name="book-detail"),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)