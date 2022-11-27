from django.shortcuts import render,get_object_or_404
from django.db.models import Q 
from store.models import Basket,BasketItem,Item,HistoryItem
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator
from operator import attrgetter
# Create your views here.
def ItemDetails(request, item_name):
    item = get_object_or_404(Item, name=item_name)
    user = request.user

    if request.method == "POST":
        user = request.user
        name = request.POST['name']
        price = request.POST['price']
        size = request.POST['size']
        quantity = request.POST['quantity']
        picture = request.POST['picture']
        basket, created = Basket.objects.get_or_create(user=user)
        basketItem = BasketItem(user=user, name=name, price=price, size=size, quantity=quantity,basket=basket, picture=picture)
        basketItem.save()

        return HttpResponseRedirect(reverse('basket', args=[user]))


    template = loader.get_template('item_details.html')

    context = {
        'item':item,
    }

    return HttpResponse(template.render(context, request))



def Item_search(search_entry=None):
	searchlist = []
	searchitems = search_entry.split(" ") 
	for i in searchitems:

		items = Item.objects.filter(
				Q(name__icontains=i) 
			).distinct()

		for item in items:
			searchlist.append(item)
	return list(set(searchlist))

def storefront(request):
	user = request.user

	context = {}
	search_entry = ""
	if request.GET:
		search_entry = request.GET.get('q', '')
		context['search_entry'] = str(search_entry)

	Items = sorted(Item_search(search_entry), key=attrgetter('added'), reverse=True)

	page = request.GET.get('page', 1)
	Items_paginator = Paginator(Items, 10)
	Items = Items_paginator.page(page)
	

	template = loader.get_template('index.html')
	context['item'] = Items

	return HttpResponse(template.render(context, request))


def Basket_view(request):
    context ={}
    user = request.user
    basket, created = Basket.objects.get_or_create(user=user)
    try:
        basket_items = BasketItem.objects.filter(basket=basket)
        page = request.GET.get('page', 1)
        basket_paginator = Paginator(basket_items, 10)
        basket_items = basket_paginator.page(page)
        total_price = 0
        for each in basket_items:
            total_price = total_price + (each.price*each.quantity)
        context['item'] = basket_items
        context['total_price'] = total_price
    except BasketItem.DoesNotExist:
        pass
    template = loader.get_template('basket.html')
    return HttpResponse(template.render(context, request))


def Addtobasket(request):
    if request.method == "POST":
        user = request.user
        price = request.POST['price']
        size = request.POST['size']
        quantity = request.POST['quantity']
        name = request.POST['name']
        basket, created = Basket.objects.get_or_create(user=user)
        basket.save()
        basket_item = BasketItem(user = user, basket=basket, price=price, size=size, quantity=quantity, name=name)
        basket_item.save()

        return HttpResponseRedirect(reverse('basket'))

def purchase(request):
    user= request.user
    basket = Basket.objects.get(user=user)
    if request.method == "POST":
        for each in BasketItem.objects.filter(basket=basket):
            name=each.name
            price=each.price
            size=each.size
            quantity=each.quantity
            purchased = HistoryItem(user=user,price=price, size=size, quantity=quantity, name=name)
            purchased.save()
            each.delete()

    return HttpResponseRedirect(reverse('basket'))

def contact(request):
    user=request.user
    
    
    context = {'user': user,}


    return render (request, 'contact.html', context=context)


def aboutus(request):
    user=request.user
    
    
    context = {'user': user,}


    return render (request, 'aboutus.html', context=context)



def store(request):
	user = request.user

	context = {}
	search_entry = ""
	if request.GET:
		search_entry = request.GET.get('q', '')
		context['search_entry'] = str(search_entry)

	Items = sorted(Item_search(search_entry), key=attrgetter('added'), reverse=True)

	page = request.GET.get('page', 1)
	Items_paginator = Paginator(Items, 10)
	Items = Items_paginator.page(page)
	

	template = loader.get_template('store.html')
	context['item'] = Items

	return HttpResponse(template.render(context, request))
    
def purchase_history(request):
    context ={}
    user = request.user
    try:
        historyitems = HistoryItem.objects.filter(user=user)
        page = request.GET.get('page', 1)
        basket_paginator = Paginator(historyitems, 10)
        historyitems = basket_paginator.page(page)
        context['item'] = historyitems
    except HistoryItem.DoesNotExist:
        pass
    template = loader.get_template('purchase_history.html')
    return HttpResponse(template.render(context, request))

def remove(request,item_id):
    basketitems = BasketItem.objects.get(id=item_id)
    basketitems.delete()

    

    return HttpResponseRedirect(reverse('basket'))


