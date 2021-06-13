from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Book
# Create your views here.
def Book(request):
    books = Book.objects.all(request)
    
    book_paginator = Paginator(books, 20)
    
    page_number = request.GET.get('page')
    page = book_paginator.get_page(page_number)
    
    context = {
        'count': book_paginator.count(),
        'page': page
    }
    return render(request, 'books/index.html', context)