from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Review
from .forms import ReviewForm
# Create your views here.

def book_list(request):
    reviews = Review.objects.all()
    return render(request, 'review/book_list.html', {'reviews': reviews })

# def book_create(request):
    # if request.method == 'POST':
    #     title = request.POST['title']
    #     rating = request.POST['rating']
    #     description = request.POST['description']

    #     if title == '' :
    #         return render(request, 'review/book_create.html', {'error_title' : 'Please fill title of the book'})

    #     if rating == '' :
    #         return render(request, 'review/book_create.html', {'error_rating' : 'Please fill rating of the book'})

    #     review = Review(book_title = title, rating = rating, detail = description)
    #     review.save()
    #     return redirect('book_list')

    #return render(request, 'review/book_create.html')

def book_create(request):
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():        
            
            o = form.save(commit=False)
            o.rating = 100
            o.save()

            return redirect('book_list')


    return render(request, 'review/book_create.html' , {'form': form})

def book_update(request, id):
    review = Review.objects.get(id = id)
    form = ReviewForm(instance=review)


    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review )
        if form.is_valid():
            form.save()
            return redirect('book_list')

    return render(request, 'review/book_create.html' , {'form': form})

def book_delete(request, id):
    review = Review.objects.get(id = id)

    if request.method == 'POST':
        review.delete()
        return redirect('book_list')

    return render(request, 'review/book_delete_confirm.html' , {"review": review})
