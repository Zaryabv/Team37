from django.contrib import admin
from store.models import Basket,Item,BasketItem,HistoryItem

admin.site.register(Basket)
admin.site.register(Item)
admin.site.register(BasketItem)
admin.site.register(HistoryItem)