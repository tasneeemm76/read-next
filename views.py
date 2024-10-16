from .forms import CustomerDetailsForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .models import CustomerDetails
from .forms import BookForm
from .forms import ReviewForm
from django.contrib import messages
from .models import Book, Review
from .forms import ReviewForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username and password combination exists in the database
        if CustomerDetails.objects.filter(username=username, password=password).exists():
            request.session['username'] = username
            return redirect('index_with_username', username=username)
        else:
            # Redirect to sign-in page if login credentials are invalid
            return redirect('signup')
    
    # Render the login form template for GET requests
    return render(request, 'login.html')

from django.shortcuts import render

def index(request, username=None):
  
    username = request.session.get('username', '')  # Retrieve username from session

        
    return render(request, 'index.html', {'username': username})




def search_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        search_results = Book.objects.filter(title__icontains=search_query)
        return render(request, 'search_results.html', {'search_results': search_results, 'search_query': search_query})
    else:
        return render(request, 'search_results.html')



def customer_details(request):
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # Check if the username already exists
            if CustomerDetails.objects.filter(username=username).exists():
                # If the username already exists, display an error message
                messages.error(request, 'Username already exists. Please choose a different one.')
            else:
                form.save()
                return redirect('login')  # Redirect to the 'login' URL pattern
    else:
        form = CustomerDetailsForm()
    return render(request, 'customer_details.html', {'form': form, })



def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # Include request.FILES for handling files
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})


def book_list(request):
    books = Book.objects.all()
    username = request.session.get('username') 
    
    # Handle review form submission
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Get the username from the request
            if username:
                # Get the user object from CustomerDetails model
                user = CustomerDetails.objects.filter(username=username).first()
                if user:
                    # Get the user ID from the user object
                    user_id = user.pk

                    # Save the review with the associated user ID and book
                    Review.objects.create(book=form.cleaned_data['book'], user_id=user_id, comment=form.cleaned_data['comment'])

                    # Redirect back to the book list page
                    return redirect('all-books')
                else:
                    # If username is not valid, display an alert message
                    messages.error(request, 'Username not found.')
            else:
                # If username is not provided, display an alert message
                messages.error(request, 'You must provide a username to leave a review.')
        else:
            # If form is not valid, display an alert message
            messages.error(request, 'Invalid review form data.')
    else:
        form = ReviewForm()

    return render(request, 'book_list.html', {'books': books, 'username': username, 'form': form})




def book_details(request, book_id):
    # Retrieve the book object from the database using the book ID
    book = get_object_or_404(Book, bookID=book_id)
    
    # Fetch existing reviews related to the book
    reviews = Review.objects.filter(book=book)
    
    # Handle review form submission
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None
            comment = form.cleaned_data['comment']
            review = Review.objects.create(book=book, user=user, comment=comment)
            return redirect('book_details', book_id=book_id)
    else:
        form = ReviewForm()
    
    return render(request, 'book_details.html', {'book': book, 'reviews': reviews, 'form': form})

#BOOKS

def romantic_books(request):
    books = Book.objects.filter(category='romantic')  
    username = request.session.get('username') 
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if username:
                # Get the user object from CustomerDetails model
                user = CustomerDetails.objects.filter(username=username).first()
                if user:
                    # Get the user ID from the user object
                    user_id = user.pk
                    # Save the review with the associated user ID and book
                    Review.objects.create(book=form.cleaned_data['book'], user_id=user_id, comment=form.cleaned_data['comment'])

                    return redirect('romantic_books')
                else:
                    messages.error(request, 'Username not found.')
        else:
            messages.error(request, 'Invalid review form data.')
    else:
        form = ReviewForm()
    
    return render(request, 'romantic_books.html', {'books': books, 'username': username,'form':form})

def mystery_books(request):
    books = Book.objects.filter(category='mystery')  
    username = request.session.get('username') 
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if username:
                # Get the user object from CustomerDetails model
                user = CustomerDetails.objects.filter(username=username).first()
                if user:
                    # Get the user ID from the user object
                    user_id = user.pk
                    # Save the review with the associated user ID and book
                    Review.objects.create(book=form.cleaned_data['book'], user_id=user_id, comment=form.cleaned_data['comment'])

                    return redirect('mystery_books')
                else:
                    messages.error(request, 'Username not found.')
        else:
            messages.error(request, 'Invalid review form data.')
    else:
        form = ReviewForm()
    
    return render(request, 'mystery_books.html', {'books': books, 'username': username,'form':form})

def selfhelp_books(request):
    books = Book.objects.filter(category='selfhelp')  
    username = request.session.get('username') 
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if username:
                # Get the user object from CustomerDetails model
                user = CustomerDetails.objects.filter(username=username).first()
                if user:
                    # Get the user ID from the user object
                    user_id = user.pk
                    # Save the review with the associated user ID and book
                    Review.objects.create(book=form.cleaned_data['book'], user_id=user_id, comment=form.cleaned_data['comment'])

                    return redirect('selfhelp_books')
                else:
                    messages.error(request, 'Username not found.')
        else:
            messages.error(request, 'Invalid review form data.')
    else:
        form = ReviewForm()
    
    return render(request, 'selfhelp_books.html', {'books': books, 'username': username,'form':form})


def fantasy_books(request):
    books = Book.objects.filter(category='fantasy')  
    username = request.session.get('username') 
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if username:
                # Get the user object from CustomerDetails model
                user = CustomerDetails.objects.filter(username=username).first()
                if user:
                    # Get the user ID from the user object
                    user_id = user.pk
                    # Save the review with the associated user ID and book
                    Review.objects.create(book=form.cleaned_data['book'], user_id=user_id, comment=form.cleaned_data['comment'])

                    return redirect('fiction_books')
                else:
                    messages.error(request, 'Username not found.')
        else:
            messages.error(request, 'Invalid review form data.')
    else:
        form = ReviewForm()
    return render(request, 'fantasy_books.html', {'books': books, 'username': username,'form': form})

def fiction_books(request):
    books = Book.objects.filter(category='fiction')  
    username = request.session.get('username') 
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if username:
                # Get the user object from CustomerDetails model
                user = CustomerDetails.objects.filter(username=username).first()
                if user:
                    # Get the user ID from the user object
                    user_id = user.pk
                    # Save the review with the associated user ID and book
                    Review.objects.create(book=form.cleaned_data['book'], user_id=user_id, comment=form.cleaned_data['comment'])

                    return redirect('fiction_books')
                else:
                    messages.error(request, 'Username not found.')
        else:
            messages.error(request, 'Invalid review form data.')
    else:
        form = ReviewForm()
    return render(request, 'fiction_books.html', {'books': books, 'username': username,'form': form})

from django.db.models import Q
def horror_books(request):
    books = Book.objects.filter(Q(category__iexact='horror'))
    username = request.session.get('username') 
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if username:
                # Get the user object from CustomerDetails model
                user = CustomerDetails.objects.filter(username=username).first()
                if user:
                    # Get the user ID from the user object
                    user_id = user.pk
                    # Save the review with the associated user ID and book
                    Review.objects.create(book=form.cleaned_data['book'], user_id=user_id, comment=form.cleaned_data['comment'])

                    return redirect('horror_books')
                else:
                    messages.error(request, 'Username not found.')
        else:
            messages.error(request, 'Invalid review form data.')
    else:
        form = ReviewForm()
    return render(request, 'horror_books.html', {'books': books, 'username': username,'form': form})


def comic_books(request):
    books = Book.objects.filter(category='comic')  
    username = request.session.get('username') 
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if username:
                # Get the user object from CustomerDetails model
                user = CustomerDetails.objects.filter(username=username).first()
                if user:
                    # Get the user ID from the user object
                    user_id = user.pk
                    # Save the review with the associated user ID and book
                    Review.objects.create(book=form.cleaned_data['book'], user_id=user_id, comment=form.cleaned_data['comment'])

                    return redirect('comic_books')
                else:
                    messages.error(request, 'Username not found.')
        else:
            messages.error(request, 'Invalid review form data.')
    else:
        form = ReviewForm()

    return render(request, 'comic_books.html', {'books': books, 'username': username, 'form': form})


#WISHLIST
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Wishlist

def wishlist(request):
    username = request.session.get('username')

    # Get the user object based on the username
    user = CustomerDetails.objects.get(username=username)
    
    try:
        # Fetch the wishlist items associated with the user ID
        wishlist_items = Wishlist.objects.filter(user_id=user.id)
        return render(request, 'wishlist.html', {'wishlist_items': wishlist_items, 'username': username})
    except Wishlist.DoesNotExist:
        return render(request, 'wishlist.html', {'username': username, 'wishlist_not_created': True})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist, Book, CustomerDetails

def add_to_wishlist(request, book_id):
    # Fetch the username from the session
    username = request.session.get('username')

    # Get the corresponding user object from the database
    user = CustomerDetails.objects.get(username=username)

    # Retrieve the book object
    book = get_object_or_404(Book, bookID=book_id)

    if request.method == 'POST':
        # Create a new Wishlist object and save it to the database
        wishlist_item = Wishlist.objects.create(user=user, book=book)

        # Redirect the user to the wishlist page
        return redirect('wishlist')
    else:
        return render(request, 'book_details.html', {'book': book})


def remove_book_from_wishlist(request, item_id):
    # Get the wishlist item object or return 404 error if not found
    item = get_object_or_404(Wishlist, pk=item_id)
    
    # Delete the item from the database
    item.delete()
    
    # Redirect back to the wishlist page
    return redirect('wishlist')


#LOGOUT

def logout_view(request):
    # Clear the username from the session
    if 'username' in request.session:
        del request.session['username']
        messages.success(request, 'You have been successfully logged out.')
    
    # Redirect to the login page
    return redirect('login')

#email subscription 
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Send confirmation email
        send_confirmation_email(email)
        return render(request, 'confirmation.html')  # Render a page confirming subscription
    else:
        return render(request, 'index.html')

def send_confirmation_email(email):
    subject = 'Subscription Confirmation'
    message = 'Thanks for subscribing to our newsletter!'
    sender = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, sender, recipient_list)


#RECOMMENDATION SYSTEM
from django.shortcuts import render
from .models import Wishlist, Book, CustomerDetails

def recommended_books(request):
    # Check if a wishlist exists for the current user
    username = request.session.get('username')
    if username:
        try:
            # Retrieve the wishlist for the current user
            wishlist = Wishlist.objects.filter(user__username=username)
            if wishlist.exists():
                # Initialize sets to collect unique categories and authors
                categories = set()
                authors = set()
                # Iterate over each book in the wishlist
                for item in wishlist:
                    categories.add(item.book.category)
                    authors.add(item.book.author)
                
                # Find books with similar categories or authors
                recommended_books = Book.objects.filter(category__in=categories) | Book.objects.filter(author__in=authors)
                context = {'recommended_books': recommended_books}
            else:
                # Wishlist is empty, recommend one book from each category
                categories = Book.objects.values_list('category', flat=True).distinct()
                recommended_books = [Book.objects.filter(category=category).first() for category in categories]
                context = {'recommended_books': recommended_books}
        except Wishlist.DoesNotExist:
            # Wishlist does not exist
            context = {'error_message': 'Wishlist not found.'}
    else:
        # User is not logged in
        context = {'error_message': 'User not logged in.'}
    
    return render(request, 'recommended_books.html', context)
