from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from linktosite.views import New_link_view, MainView

urlpatterns = [
    path('admin_panel/', admin.site.urls, name='admin'),
    path('', MainView.as_view(), name='main_view'),
    path('new_link/', New_link_view.as_view(), name='new_link_view')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
