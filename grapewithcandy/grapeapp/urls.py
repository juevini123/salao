from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastro',views.cadastro,name='cadastro'),
    path('docad/',views.docad, name='docad'),
]
#views= funcoes a serem realizadas