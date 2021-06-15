from django.urls import path
from . import views 

urlpatterns = [
	path('', views.home, name="home"),
	path('post/<int:pk>/', views.detalhe_postagem, name="detalhe_postagem"),
	path('post/new/', views.adicionar_postagem, name="adicionar_postagem"),
	path('post/edit_postagem/<int:pk>', views.edit_postagem, name="edit_postagem"),
	path('post/del_postagem/<int:pk>', views.del_postagem, name="del_postagem")
]