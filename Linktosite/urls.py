from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from linktosite.views import New_link_view, New_category_view, MainView

urlpatterns = [
    path('admin_panel/', admin.site.urls, name='admin'),
    path('users/', include('users.urls')),
    path('new_link/', login_required(New_link_view.as_view()), name='new_link_view'),
    path('new_category/', login_required(New_category_view.as_view()),
         name='new_category_view'),
    path('', MainView.as_view(), name='main_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
