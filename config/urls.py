from django.contrib import admin
from django.urls import path, include, re_path
from account.views import Login, Register, activate
from django.conf import settings # just for debug mode without a web server
from django.conf.urls.static import static # just for debug mode without a web server

urlpatterns = [
    path('', include('blogcore.urls')),
    path('', include('django.contrib.auth.urls')),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    #re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
]

# just for debug mode without a web server
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
