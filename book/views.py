from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response

from rest_framework.views import APIView

from .serializers import BookSerializer
from .models import Book


# Class - based view


#  Concreate API view

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Generic API view

class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# Class based view APIView

class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f'Returned {len(serializer_data)} books',
            'data': serializer_data,
        }
        return Response(data)

class BookCreateView(APIView):

    def post(self, request):
        data = request.data
        print(data)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            print(data)
            serializer.save()
            data = {
                'status': 'Books are saved to the database',
                "books": data,
            }
            print(data)
            return Response(data)


class BookDetailView1(APIView):  # ishlatilmayapti
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            print(book)
            serializer_data = BookSerializer(book).data
            print(serializer_data)
            data = {
                'status': f'Returned {len(serializer_data)}',
                'book': serializer_data,
            }
            print(data)
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {'status': 'False',
                 'message': 'Book is not found',
                 }, status=status.HTTP_404_NOT_FOUND
            )
class BookDetailView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        serializer_data = BookSerializer(book).data
        data = {
            'status': True,
            'book': serializer_data,
        }
        print(data)
        return Response(data, status=status.HTTP_200_OK)


 #Delete API View 2 ta
class BookDeleteView1(APIView):  # ishlatilmayapti

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            print(book)
            book.delete()
        except Exception:
            return Response(
                {
                    'status': 'False',
                    'message': 'Book is not found',
                },
                status=status.HTTP_404_NOT_FOUND
            )

class BookDeleteView(APIView):
    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = book.delete()
        return Response(
            {
                'status': 'True',
                'message': f'Book {data} has been deleted'
            }
        )


# Update API VIEW
class BookUpdateView1(APIView):  # ishlatilmayapti
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        print(book)
        data = request.data
        print(data)
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            print(book_saved)
            return Response(
                {'status': 'Updated',
                 'message': f'Book {book_saved} updated successfully'}
            )
class BookUpdateView(APIView):
    def put(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            data = request.data
            serializer = BookSerializer(instance=book, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                book_saved = serializer.save()
                return Response(
                    {'status': 'Updated',
                     'message': F'Book {book_saved} updated successfully'}
                )
        except Exception:
            return Response(
                {'status': 'False'}
            )

# VIewset va routerlar

#class BookViewset(viewsets.ModelViewSet):
#    queryset = Book.objects.all()
#    serializer_class = BookSerializer

#class BookViewSet(viewsets.ViewSet):
#    def list(self, request):
#        books = Book.objects.all()
#        serializer = BookSerializer(books, many=True)
#        return Response(serializer.data)
#    def retrieve(self, request, pk):
#        queryset = Book.objects.get(id=pk)
#        book = get_object_or_404(queryset, id=pk)
#        serializer = BookSerializer(book)
#        return Response(serializer.data)

# function based view
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)




