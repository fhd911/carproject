from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="العميل")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="إجمالي السعر")
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'قيد المعالجة'),
            ('completed', 'مكتمل'),
            ('cancelled', 'ملغي'),
        ],
        default='pending',
        verbose_name="حالة الطلب"
    )

    def __str__(self):
        return f"طلب رقم {self.id}"

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"
