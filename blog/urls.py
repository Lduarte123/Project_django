from django.urls import path
from.import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contatos.html/', views.contatos, name='contatos'),
    path('habilidades', views.habilidades, name='habilidades'),
    path('projetos', views.projetos, name='projetos'),
    path('sobre', views.sobre, name='sobre')   
]