from django.contrib import admin
from django.urls import path, include
from account.views import Login
from django.conf import settings # just for debug mode without a web server
from django.conf.urls.static import static # just for debug mode without a web server

urlpatterns = [
    path('', include('blogcore.urls')),
    path('', include('django.contrib.auth.urls')),
    path('login/', Login.as_view(), name='login'),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
]

# just for debug mode without a web server
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
