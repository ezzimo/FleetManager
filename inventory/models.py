from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .constants import THRESHOLD, ORDER_QUANTITY


class SparePart(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    minimum_quantity = models.IntegerField(null=True, blank=True, help_text="The minimum quantity before a re-order is triggered.")
    reorder_trigger = models.BooleanField(null=True, blank=True, default=False, help_text="True if a re-order needs to be triggered.")
    last_order_date = models.DateField(null=True, blank=True, help_text="The date of the last order for this part.")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.quantity < THRESHOLD:
            Order.objects.create(spare_part=self, quantity=self.quantity or ORDER_QUANTITY)
            self.last_order_date = timezone.now()
        super().save(*args, **kwargs)


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        ORDERED = 'ordered', _('Ordered')
        RECEIVED = 'received', _('Received')
        CANCELLED = 'cancelled', _('Cancelled')

    spare_part = models.ForeignKey(SparePart, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
    order_date = models.DateField(default=timezone.now)
    expected_delivery_date = models.DateField()
    received_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.ORDERED)

    def __str__(self):
        return f'Order #{self.id} for {self.spare_part.name}'
    
    def save(self, *args, **kwargs):
        if self.status == self.OrderStatus.RECEIVED:
            self.spare_part.reorder_trigger = False
            self.spare_part.save()
        elif self.status == self.OrderStatus.ORDERED:
            self.spare_part.reorder_trigger = True
            self.spare_part.save()
        super().save(*args, **kwargs)