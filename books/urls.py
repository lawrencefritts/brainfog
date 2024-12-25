from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # List views
    path('', views.ShelfListView.as_view(), name='shelf_list'),
    
    # Book URLs
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/add/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    
    # Author URLs
    path('author/', views.AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('author/add/', views.AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
    
    # Series URLs
    path('series/', views.SeriesListView.as_view(), name='series_list'),
    path('series/<int:pk>/', views.SeriesDetailView.as_view(), name='series_detail'),
    path('series/add/', views.SeriesCreateView.as_view(), name='series_create'),
    path('series/<int:pk>/edit/', views.SeriesUpdateView.as_view(), name='series_update'),
    path('series/<int:pk>/delete/', views.SeriesDeleteView.as_view(), name='series_delete'),
]

