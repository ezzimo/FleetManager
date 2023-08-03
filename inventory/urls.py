from django.urls import path
from .views import SparePartsListView, SparePartDetailView, SparePartCreateView, SparePartUpdateView, SparePartDeleteView, OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView

app_name = 'inventory'

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/new/', OrderCreateView.as_view(), name='order_new'),
    path('order/<int:pk>/edit/', OrderUpdateView.as_view(), name='order_edit'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
    path('spare_parts/', SparePartsListView.as_view(), name='spare_parts_list'),
    path('spare_part/<int:pk>/', SparePartDetailView.as_view(), name='spare_part_detail'),
    path('spare_part/new/', SparePartCreateView.as_view(), name='spare_part_new'),
    path('spare_part/<int:pk>/edit/', SparePartUpdateView.as_view(), name='spare_part_edit'),
    path('spare_part/<int:pk>/delete/', SparePartDeleteView.as_view(), name='spare_part_delete'),
]
