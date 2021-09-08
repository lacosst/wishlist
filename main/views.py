from django.shortcuts import render, get_object_or_404

from .models import *


def index(request):
    data = Product.objects.all()
    context = {
        'data': data,
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
    print('wishlist: ', wishlist)

    context = {
        'wishlist': wishlist,
        'is_owner_list': wishlist.owner == request.user
    }
    return render(request, 'wish_list.html', context)