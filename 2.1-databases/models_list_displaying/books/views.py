from django.shortcuts import render
from books.models import Book

BOOKS = Book.objects.all()

def books_view(request):
    template = 'books/books_list.html'
    context = {'books': BOOKS}
    return render(request, template, context)

def book_view(request, date_pub):

    template = 'books/book_date.html'
    book = Book.objects.filter(pub_date=date_pub).all()
    back_page = Book.objects.all().filter(pub_date__lt=date_pub).values('pub_date').all().order_by('-pub_date').first()
    next_page = Book.objects.all().filter(pub_date__gt=date_pub).values('pub_date').all().order_by('pub_date').first()
    context = {'books': book,
               'back_page': back_page,
               'next_page': next_page,

              }
    return render(request, template, context)

