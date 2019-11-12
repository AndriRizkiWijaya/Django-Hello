from django.shortcuts import render
from django.views.generic import ListView
from products.models import Item

# Create your views here.
# CLASS BASE VIEW
class DashboardView(ListView):
    model               = Item
    template_name       = 'dashboard/dashboard.html'
    context_object_name = 'items'
    extra_context       = {'title_page':'Dashboard',}

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)
        kwarg = self.kwargs
        return super().get_context_data(**kwarg)
