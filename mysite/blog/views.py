from django.shortcuts import render
from blog.models import Postagem
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
# Create your views here.

def home(request):
	postagens = Postagem.objects.all().order_by("-data_criacao")

	return render(request, 'home.html', {'postagens': postagens})

def detalhe_postagem(request, pk):
	postagem = Postagem.objects.get(pk=pk)
	return render(request, 'detalhe_postagem.html', {'postagem': postagem})

def adicionar_postagem(request):
	#Ao salvar.
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			postagem = form.save(commit=False)
			postagem.autor = request.user
			postagem.data_publicacao = timezone.now()
			postagem.save()
			return redirect('home')
	#Primeiro Acesso.
	else:
		form = PostForm()
	return render(request, 'editar_postagem.html', {'form': form})

def edit_postagem(request, pk):
	postagem = get_object_or_404(Postagem, pk=pk)
	#Ao salvar.
	if request.method == "POST":
		form = PostForm(request.POST, instance=postagem)
		if form.is_valid():
			postagem = form.save(commit=False)
			postagem.autor = request.user
			postagem.data_publicacao = timezone.now()
			postagem.save()
			return redirect('home')
	#Primeiro Acesso.
	else:
		form = PostForm(instance=postagem)
	return render(request, 'editar_postagem.html', {'form': form})	

def del_postagem(request, pk):
	postagem = get_object_or_404(Postagem, pk=pk)
	postagem.delete()
	return redirect('home')	