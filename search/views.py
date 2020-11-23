from django.shortcuts import render
from search.documents import BookDocument

# Create your views here.

def search(request):

    q = request.GET.get('q')

    if q:
        books = BookDocument.search().query("match_phrase", name = q)
    else:
        books = ''
    return render(request, 'book/search_results.html', {'books': books})