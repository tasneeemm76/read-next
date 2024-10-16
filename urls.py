"""
URL configuration for mini_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('logout/', views.logout_view, name='logout'),
    path('add_to_wishlist/<int:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('romantic_books/', views.romantic_books, name='romantic_books'),
    path('fiction_books/', views.fiction_books, name='fiction_books'),
    path('horror_books/', views.horror_books, name='horror_books'),
    path('mystery_books/', views.mystery_books, name='mystery_books'),
    path('selfhelp_books/', views.selfhelp_books, name='selfhelp_books'),
    path('comic_books', views.comic_books, name='comic_books'),
    path('fantasy_books', views.fantasy_books, name='fantasy_books'),
    path('recommended-books/', views.recommended_books, name='recommended_books'),

    path('signup', views.customer_details, name="signup"),
    path('search', views.search_view, name="search"),
    path('login/', views.login_view, name='login'),
    path('create/', views.create_book, name='create_book'),
    path('all-books', views.book_list, name='all-books'),
    path('<str:username>/', views.index, name='index_with_username'),
    path('book/<int:book_id>/', views.book_details, name='book_details'),
    path('remove_from_wishlist/<int:item_id>/', views.remove_book_from_wishlist, name='remove_from_wishlist'),
    path('index', views.index, name='index'),
    path('subscribe/', views.subscribe, name='subscribe'),
]


# Serve media fi
# les during development
from django.conf import settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)