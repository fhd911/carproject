from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # تعريف التطبيقات الثلاثة
    path('accounts/', include('accounts.urls')),
    path('shop/', include('shop.urls')),
    path('orders/', include('orders.urls')),
]
