from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="اسم التصنيف"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="وصف التصنيف"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "التصنيف"
        verbose_name_plural = "التصنيفات"


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="التصنيف"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="اسم المنتج"
    )
    description = models.TextField(
        verbose_name="وصف المنتج"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر"
    )
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="صورة المنتج"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "المنتج"
        verbose_name_plural = "المنتجات"
