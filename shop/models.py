from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم التصنيف")
    description = models.TextField(verbose_name="الوصف", blank=True, null=True)

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        verbose_name="التصنيف"
    )
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    description = models.TextField(verbose_name="الوصف", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    image = models.ImageField(upload_to="products/", verbose_name="صورة المنتج", blank=True, null=True)

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
