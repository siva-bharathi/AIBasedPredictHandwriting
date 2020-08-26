from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.photo_get,name = 'photo_get'),

    path('process',views.home,name = 'home'),
] 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
