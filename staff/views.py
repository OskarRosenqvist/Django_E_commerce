from django.shortcuts import render
from django.views import generic
from django.contrib.auth import mixins
from cart.models import Order
from .mixins import StaffUserMixin


class StaffView(mixins.LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name = 'staff/staff.html'
    queryset = Order.objects.filter(ordered=True).order_by('-ordered_date')
    paginate_by = 20
    context_object_name = 'orders'
