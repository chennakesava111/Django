from books.models import Book, Review
from django.shortcuts import redirect, render, get_object_or_404

def index(request):
    dbData = Book.objects.all()
    context = {'books':dbData}
    return render(request, 'index.html', context)

def show(request,id):
    singleBook = get_object_or_404(Book,pk=id)
    reviews = Review.objects.all()
    context = {'book':singleBook,'reviews':reviews}
    return render(request, 'show.html', context)

def review(request):
    body = request.POST['review']
    newReview = Review(body=body)
    newReview.save()
    return redirect('/book')

def fun1(request):
    