from django import forms
from .models import CustomerDetails
from .models import Review, Book


class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = [ 'first_name' ,'last_name','email','phone','username' , 'password' ]
   

class SuperuserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
 


from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'publication_date', 'image','category']


from django import forms
from .models import Review, Wishlist

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['book','comment']

