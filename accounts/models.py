from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        verbose_name="المستخدم"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="رقم الجوال",
        blank=True, null=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="العنوان",
        blank=True, null=True
    )

    class Meta:
        verbose_name = "الملف الشخصي"
        verbose_name_plural = "الملفات الشخصية"

    def __str__(self):
        return f"{self.user.username}"
