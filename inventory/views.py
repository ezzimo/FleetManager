from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import SparePart, Order
from .forms import OrderForm, SparePartForm
from .constants import THRESHOLD, ORDER_QUANTITY


class SparePartsListView(ListView):
    model = SparePart
    template_name = 'inventory/spare_parts_list.html'
    context_object_name = 'spare_parts'


class SparePartDetailView(DetailView):
    model = SparePart
    template_name = 'inventory/spare_part_detail.html'
    context_object_name = 'spare_part'


class SparePartCreateView(CreateView):
    model = SparePart
    form_class = SparePartForm
    template_name = 'inventory/spare_part_edit.html'

    def get_success_url(self):
        return reverse_lazy('inventory:spare_part_detail', args=[self.object.id])
    
    def form_valid(self, form):
        response = super().form_valid(form)
        spare_part = self.object
        if spare_part.quantity < THRESHOLD:
            Order.objects.create(spare_part=spare_part, quantity=ORDER_QUANTITY or spare_part.quantity)
        return response


class SparePartUpdateView(UpdateView):
    model = SparePart
    form_class = SparePartForm
    template_name = 'inventory/spare_part_edit.html'

    def get_success_url(self):
        return reverse_lazy('inventory:spare_part_detail', args=[self.object.id])

    def form_valid(self, form):
        response = super().form_valid(form)
        spare_part = self.object
        if spare_part.quantity < THRESHOLD:
            Order.objects.create(spare_part=spare_part, quantity=ORDER_QUANTITY or spare_part.quantity)
        return response


class SparePartDeleteView(DeleteView):
    model = SparePart
    template_name = 'inventory/spare_part_confirm_delete.html'
    success_url = reverse_lazy('inventory:spare_parts_list')


class OrderListView(ListView):
    model = Order
    template_name = 'inventory/order_list.html'
    context_object_name = 'orders'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'inventory/order_detail.html'
    context_object_name = 'order'


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'inventory/order_form.html'

    def get_success_url(self):
        return reverse_lazy('inventory:order_detail', args=[self.object.id])


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'inventory/order_form.html'

    def get_success_url(self):
        return reverse_lazy('inventory:order_detail', args=[self.object.id])


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'inventory/order_confirm_delete.html'
    success_url = reverse_lazy('inventory:order_list')
