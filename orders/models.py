from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="المستخدم"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الطلب"
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name="تم الدفع؟"
    )

    def __str__(self):
        return f"طلب رقم {self.id}"

    class Meta:
        verbose_name = "الطلب"
        verbose_name_plural = "الطلبات"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="الطلب"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="المنتج"
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="الكمية"
    )

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"
