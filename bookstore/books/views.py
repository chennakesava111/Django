from django.shortcuts import render
import json

booksData = open("C:/Users/cv20264/Desktop/BookStoreProject/books.json").read()

data = json.loads(booksData)

def index(request):
    context = {'books':data}
    return render(request, 'index.html', context)

def show(request,id):
    singleBook = list()
    for book in data:
        if book['id'] == id:
            singleBook = book
    context = {'book':singleBook}
    return render(request, 'show.html', context)