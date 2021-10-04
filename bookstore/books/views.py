from books.models import Book, Review
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView


class BookListView(ListView):
    def get_queryset(self):
        return Book.objects.all()


def author(request,author):
    books = Book.objects.filter(authors__name=name)
    context = {'book_list':books}
    return render(request,'registration/book_list.html',context)

def review(request, id):
    if request.user.is_authenticated:
        body = request.POST['review']
        newReview = Review(body=body, book_id=id, user=request.user)
        newReview.save()
    return redirect('/book')


class BookDetailView(DetailView):
    model = Book

    def def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        return context

    




# def index(request):
#     dbData = Book.objects.all()
#     context = {'books':dbData}
#     return render(request, 'index.html', context)

# def show(request,id):
#     singleBook = get_object_or_404(Book,pk=id)
#     reviews = Review.objects.filter(book_id=id).order_by('-created_at')
#     context = {'book':singleBook,'reviews':reviews}
#     return render(request, 'show.html', context)

# def review(request, id):
#     body = request.POST['review']
#     newReview = Review(body=body, book_id=id)
#     newReview.save()
#     return redirect('/book')

    