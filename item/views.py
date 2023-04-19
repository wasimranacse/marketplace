from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Item
from .forms import NewItemForm

def detailView(request, pk):
    item = get_object_or_404(Item, pk=pk)

    # show related items
    related_items = Item.objects.filter(
        category=item.category, 
        is_sold=False
    ).exclude(pk=pk)[0:3]

    return render(request, 'item/product-single.html',{
        'item': item,
        'related_items': related_items,
    })

@login_required
def addNewItem(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    return render(request, 'item/form.html',{
        'form': form,
        'title': 'Add New Item',
    })