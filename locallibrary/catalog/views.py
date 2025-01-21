from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # Romance books (genre.name = 'romance', case insensitive match)
    num_romance_books = Book.objects.filter(genre__name__iexact='romance').count()
    
    # Test books (title contains test, case insensitive)
    num_test_books = Book.objects.filter(genre__name__icontains='test').count()


    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_romance_books': num_romance_books,
        'num_test_books': num_test_books,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
