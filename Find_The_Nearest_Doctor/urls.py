from django.urls import path
from . import views

urlpatterns = [
   path('Followers', views.t, name="Followers"),
    path('Doctors',views.two,name='Doctors'),
   path('Diseases',views.one,name='Diseases'),
   # path('k',views.k,name='k'),


  
]
