from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView

# @api_view(['GET'])
# def bookList(request):
#     if request.method == "GET":
#         bookList = Book.objects.all()
#         serializedBookList=BookSerializer(bookList,many=True)
#         return Response(serializedBookList.data)


# @api_view(['GET'])
# def getBook(request, pk):
#     if request.method == "GET":
#         book = Book.objects.get(id=pk)
#         serializedBook=BookSerializer(book,many=False)
#         return Response(serializedBook.data)


# @api_view(['POST'])
# def addBook(request):
#     if request.method == "POST":
#         newBookSerializer=BookSerializer(data=request.data)
#         if newBookSerializer.is_valid():
#             newBookSerializer.save()
#             return Response(newBookSerializer.data)
#         else:
#             return Response(newBookSerializer.errors)


# @api_view(['PATCH'])
# def updateBook(request,pk):
#     if request.method == "PATCH":
#         book=Book.objects.get(id=pk)

#         serializer=BookSerializer(book,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['DELETE'])
# def deleteBook(request,pk):
#     if request.method == "DELETE":
#         book=Book.objects.get(id=pk)
#         book.delete()
#         return Response({"deleted":pk})


class BookList(APIView):
    def get(self, request):
        bookList = Book.objects.all()
        serializedBookList = BookSerializer(bookList, many=True)
        return Response(serializedBookList.data)


class GetBook(APIView):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializedBook = BookSerializer(book, many=False)
        return Response(serializedBook.data)


class AddBook(APIView):
    def post(self, request):
        newBookSerializer = BookSerializer(data=request.data)
        if newBookSerializer.is_valid():
            newBookSerializer.save()
            return Response(newBookSerializer.data)
        else:
            return Response(newBookSerializer.errors)


class UpdateBook(APIView):
    def patch(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class DeleteBook(APIView):
    def delete(self, request, pk):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response({"deleted": pk})


# {
# "title" : "harry",
# "description" : "harry porter"
# }
