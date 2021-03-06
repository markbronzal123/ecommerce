from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('payment.urls')),
    path('', include('store.urls'))
]

if settings.DEBUG:
    urlpatterns+=[
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
