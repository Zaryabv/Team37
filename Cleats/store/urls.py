
from django.urls import path
from store.views import ItemDetails,Basket_view,storefront,Addtobasket,purchase,contact,purchase_history,remove,store,aboutus,admin_view
urlpatterns = [
path('<str:item_name>/item_details', ItemDetails, name='item_details'),
path('cart', Basket_view, name='basket'),
path('contact', contact, name='contact'),
path('', storefront, name='index'),
path(r'^purchase/$', purchase, name='purchase'),
path(r'^additem/$', Addtobasket, name='additem'),
path('<uuid:item_id>/remove', remove, name='remove'),
path('purchase_history', purchase_history, name='purchase_history'),
path('store', store, name='store'),
path('aboutus', aboutus, name='aboutus'),
path('admin', admin_view, name='admin'),
]
