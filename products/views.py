from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView
from .models import Item, OrderItem, Order

# Create your views here.
class ProductDetail(DetailView):
    model               = Item
    template_name       = 'products/product_detail.html'
    context_object_name = 'product_detail'
    extra_context       = {'title_page':'Detail Product'}

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwarg = self.kwargs
        return super().get_context_data(**kwarg)


def add_to_cart(request, slug):
    item                = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs            = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # Checking order, if order_item is in order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'This item quantity was updated to your cart')
            return redirect('Products:detail_view', slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, 'This item was added to your cart')
            return redirect('Products:detail_view', slug=slug)
    else:
        order_date = timezone.now() 
        order      = Order.objects.create(user=request.user, ordered_date=order_date)
        order.items.add(order_item)
        messages.info(request, 'This item was added to your cart')
    return redirect('Products:detail_view', slug=slug)

def remove_from_cart(request, slug):
    item     = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # Checking order, if order_item is in order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, 'This item was removed from your cart')
            return redirect('Products:detail_view', slug=slug)
        else:
            # Messaging order does not contains
            messages.info(request, 'This item was not in your cart')
            return redirect('Products:detail_view', slug=slug)    
    else:
        # Messaging user have not an order
        messages.info(request, 'Your do not have an active order')
        return redirect('Products:detail_view', slug=slug)    
    return redirect('Products:detail_view', slug=slug)