from django.shortcuts import render, redirect
from item.models import ItemCategory, Item
from .forms import SignUpForm

# Home page view 
def HomePageView(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = ItemCategory.objects.all()

    return render(request, 'index.html',{
        'categories': categories,
        'items': items,
    })

# About Us page view 
def AboutPageView(request):
    return render(request, 'about.html')

# Contact Us View 
def contactView(request):
    return render(request, 'contact.html')

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {
        'form': form
    })

