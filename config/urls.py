from django.contrib import admin
from django.urls import path, include
from django.conf import settings # just for debug mode without a web server
from django.conf.urls.static import static # just for debug mode without a web server

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogcore.urls')),
    path('account/', include('account.urls')),
]

# just for debug mode without a web server
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
