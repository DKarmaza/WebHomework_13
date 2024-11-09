from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, AuthorForm, QuoteForm
from .models import Quote, Author

def home(request):
    authors = Author.objects.all()
    return render(request, 'quotes/home.html', {'authors': authors})

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote_list.html', {'quotes': quotes})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id) 
    return render(request, 'quotes/author_detail.html', {'author': author})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'quotes/register.html', {'form': form})

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

@login_required
def delete_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if request.method == 'POST':
        quote.delete()
        return redirect('quote_list')
    return render(request, 'quotes/delete_quote_confirm.html', {'quote': quote})

@login_required
def delete_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('home')
    return render(request, 'quotes/delete_author_confirm.html', {'author': author}) 

@login_required
def edit_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    if request.method == 'POST':
        form = QuoteForm(request.POST, instance=quote)
        if form.is_valid():
            form.save()
            return redirect('quote_list')  
    else:
        form = QuoteForm(instance=quote)  
    return render(request, 'quotes/edit_quote.html', {'form': form})

@login_required
def edit_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_detail', author_id=author.id)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'quotes/edit_author.html', {'form': form, 'author': author})