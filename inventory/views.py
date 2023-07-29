from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import SparePart
from .forms import SparePartForm


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


class SparePartUpdateView(UpdateView):
    model = SparePart
    form_class = SparePartForm
    template_name = 'inventory/spare_part_edit.html'

    def get_success_url(self):
        return reverse_lazy('inventory:spare_part_detail', args=[self.object.id])


class SparePartDeleteView(DeleteView):
    model = SparePart
    template_name = 'inventory/spare_part_confirm_delete.html'
    success_url = reverse_lazy('inventory:spare_parts_list')
