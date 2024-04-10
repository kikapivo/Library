from django.views.generic.list import ListView
from .models import Book


class BooksList(ListView):
    model = Category
    #context_object_name='books'
    template_name='categories.html'
    paginate_by=2


class BookDetail(DetailView):
    model=Book
    template_name='book_detail.html'
