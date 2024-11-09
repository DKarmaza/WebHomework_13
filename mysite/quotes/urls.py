"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('quotes/', views.quote_list, name='quote_list'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('quote/<int:quote_id>/delete/', views.delete_quote, name='delete_quote'),
    path('author/<int:author_id>/delete/', views.delete_author, name='delete_author'),
    path('quote/<int:quote_id>/edit/', views.edit_quote, name='edit_quote'),
    path('author/<int:author_id>/edit/', views.edit_author, name='edit_author'),
]
