from django.urls import path
from .views import BookListAPIView, book_list_view, \
    BookDetailAPIView, BookDeleteAPIView, BookUpdateAPIView, \
    BookListCreateAPIView, BookUpdateDeleteAPIView, BookListView, \
    BookCreateView, BookDetailView, BookDeleteView, BookUpdateView



urlpatterns = [
    path('', BookListAPIView.as_view()),
    path('books/', book_list_view),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
    path('booklistcreate/', BookListCreateAPIView.as_view()),
    path('booklistupdatedelete/<int:pk>/', BookUpdateDeleteAPIView.as_view()),
    path('booklist/', BookListView.as_view()),
    path('booklist/create/', BookCreateView.as_view()),
    path('booklist/<int:pk>/', BookDetailView.as_view()),
    path('booklist/<int:pk>/delete/', BookDeleteView.as_view()),
    path('booklist/<int:pk>/update/', BookUpdateView.as_view()),

]