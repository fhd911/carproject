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
        blank=True,
        null=True,
        verbose_name="رقم الجوال"
    )

    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="العنوان"
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "ملف المستخدم"
        verbose_name_plural = "ملفات المستخدمين"
