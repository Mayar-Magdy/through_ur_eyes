from django.conf.urls.static import static 
from django.contrib import admin 
from django.urls import path , include 
from .views import chatbot 
from django.conf import settings




urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('Accounts.urls')),
    path('', include('Find_The_Nearest_Doctor.urls')),
    path('', chatbot, name='chatbot'),
    path('', include('Machine_Learning.urls')),

    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


