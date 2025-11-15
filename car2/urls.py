from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # ربط التطبيقات الثلاثة
    path('accounts/', include('accounts.urls')),
    path('shop/', include('shop.urls')),
    path('orders/', include('orders.urls')),
]

# 📌 دعم MEDIA و STATIC أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
