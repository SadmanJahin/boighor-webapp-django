from django.shortcuts import render
from .models import Book
from index.views import footerContent
# Create your views here.


def viewallBook(request):
    bookList = Book.objects.all()
    userName=[]
    for x in bookList:
        data=(Book.getUserName(Book,x.user_id))
        for y in data:
            userName.append(y[0])

    print(userName)
    context={
        'book': zip(bookList,userName),
        'footer': footerContent,
    }
    return render(request,'book/book.html',context)

def viewBookCategoryEducation(request):
    bookList = Book.objects.all().filter(bookCategory="Education")
    userName = []
    for x in bookList:
        data = (Book.getUserName(Book, x.user_id))
        for y in data:
            userName.append(y[0])

    print(userName)
    context = {
        'book': zip(bookList, userName),
        'footer': footerContent,
    }
    return render(request, 'book/book.html', context)

def viewBookCategoryScifi(request):
    bookList = Book.objects.all().filter(bookCategory="Sci-fi")
    userName = []
    for x in bookList:
        data = (Book.getUserName(Book, x.user_id))
        for y in data:
            userName.append(y[0])

    print(userName)
    context = {
        'book': zip(bookList, userName),
        'footer': footerContent,
    }
    return render(request, 'book/book.html', context)

def viewSearchedBooks(request):
    searchKeyword="None"
    if (request.method == 'POST'):
        searchKeyword = request.POST['search']
        print(searchKeyword)
    bookList = Book.objects.all().filter(bookCategory__contains=searchKeyword)|Book.objects.all().filter(bookWriter__contains=searchKeyword)|Book.objects.all().filter(bookName__contains=searchKeyword)
    userName = []
    for x in bookList:
        data = (Book.getUserName(Book, x.user_id))
        for y in data:
            userName.append(y[0])

    print(userName)
    context = {
        'book': zip(bookList, userName),
        'footer': footerContent,
    }
    return render(request, 'book/book.html', context)