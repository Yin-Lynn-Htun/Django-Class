from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book_title' , 'detail']
        labels = {
            'book_title': 'My Book',
            'rating': 'Book Rating'
        }
        error_messages = {
            'book_title': {
                'max_length': 'Title has to be shorter!'
            }
            ,
            'rating': {
                'required': 'Rating is required !!!!!!!!!!'
            }
        }