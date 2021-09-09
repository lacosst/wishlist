from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *


def index(request):
    wishlist = WishList.objects.all()
    context = {
        'wishlist': wishlist,
        'title': 'Главная страница | WishList'
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'title': 'О нас | WishList'
    }
    return render(request, 'about.html', context)


def list_page(request, pk):
    wishlist = get_object_or_404(WishList, pk=pk)
    form = ProductForm

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            wishlist.products.add(Product.objects.last())
            return redirect('wish_list_page', wishlist.pk)

    context = {
        'wishlist': wishlist,
        'is_owner_list': wishlist.owner == request.user,
        'form': form
    }
    return render(request, 'wish_list.html', context)
