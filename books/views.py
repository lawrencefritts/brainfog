from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Author, Series

class ShelfListView(ListView):
    model = Book
    template_name = 'books/shelf_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        print("All books found:", list(books))
        
        context['to_read'] = books.filter(book_status='TR')
        print("To Read books:", list(context['to_read']))
        
        context['to_acquire'] = books.filter(book_status='TA')
        print("To Acquire books:", list(context['to_acquire']))
        
        context['finished'] = books.filter(book_status='F')
        print("Finished books:", list(context['finished']))
        
        context['not_for_me'] = books.filter(book_status='N4')
        print("Not For Me books:", list(context['not_for_me']))
        
        print("Final context data:", {k: list(v) if hasattr(v, '__iter__') and not isinstance(v, str) else v 
                                    for k, v in context.items()})
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'series', 'series_order', 'book_status', 'genre', 'book_type', 'favorite']
    success_url = reverse_lazy('books:shelf_list')

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'series', 'series_order', 'book_status', 'genre', 'book_type', 'favorite']
    success_url = reverse_lazy('books:shelf_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:shelf_list')

class AuthorListView(ListView):
    model = Author
    template_name = 'books/author_list.html'
    context_object_name = 'authors'

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'books/author_form.html'
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('books:author_list')

class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'books/author_form.html'
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('books:author_list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'books/author_confirm_delete.html'
    success_url = reverse_lazy('books:author_list')

class SeriesListView(ListView):
    model = Series
    template_name = 'books/series_list.html'
    context_object_name = 'series'

class SeriesCreateView(CreateView):
    model = Series
    template_name = 'books/series_form.html'
    fields = ['name']
    success_url = reverse_lazy('books:series_list')

class SeriesUpdateView(UpdateView):
    model = Series
    template_name = 'books/series_form.html'
    fields = ['name']
    success_url = reverse_lazy('books:series_list')

class SeriesDeleteView(DeleteView):
    model = Series
    template_name = 'books/series_confirm_delete.html'
    success_url = reverse_lazy('books:series_list')

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/author_detail.html'
    context_object_name = 'author'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.filter(author=self.object).order_by('title')
        
        # Add status display names
        context['status_names'] = {
            'TR': 'To Read',
            'TA': 'To Acquire',
            'F': 'Finished',
            'N4': 'Not For Me'
        }
        
        # Group books by status
        context['to_read'] = books.filter(book_status='TR')
        context['to_acquire'] = books.filter(book_status='TA') 
        context['finished'] = books.filter(book_status='F')
        context['not_for_me'] = books.filter(book_status='N4')
        
        return context

class SeriesDetailView(DetailView):
    model = Series
    template_name = 'books/series_detail.html'
    context_object_name = 'series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(series=self.object).order_by('series_order')
        return context
