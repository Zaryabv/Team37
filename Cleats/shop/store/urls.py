

from django.urls import path
from store.views import ItemDetails,Basket_view,storefront,Addtobasket,purchase
urlpatterns = [
path('<str:item_name>/item_details', ItemDetails, name='item_details'),
path('basket_view', Basket_view, name='basket'),
path('', storefront, name='index'),
path(r'^purchase/$', purchase, name='purchase'),
path(r'^additem/$', Addtobasket, name='additem'),
]
