from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineAdminInline(admin.TabularInline): # StackedInline is another option here
    
    model = OrderLineItem
    
class OrderAdmin(admin.ModelAdmin):
    
    inlines = (OrderLineAdminInline, ) # the admin interface has the ability to edit more than one model on a single page. this is known as inlines
    
    
admin.site.register(Order, OrderAdmin)