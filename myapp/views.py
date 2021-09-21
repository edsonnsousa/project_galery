import imghdr

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ImageForm
from .models import Image


# Create your views here.
@login_required
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html', {'img': img, 'form': form})


'''def delete_foto(request, id):
    if request.method == "POST":
        img = Image.objects.get(id=id)
        img.delete()
    return render(request, 'myapp/home.html')
'''


@login_required
def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

@login_required
def delete(request, list_id):

    Image.objects.get(pk=list_id).delete()

    return render(request, 'myapp/exclusao.html')

def solicitacao(request):

        if request.method == "POST":
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        form = ImageForm()
        img = Image.objects.all()
        return render(request, 'myapp/solicitacao.html', {'img': img, 'form': form})


def aprovado(request,list_id):
    Image.objects.filter(pk=list_id).update(tipo=1)

    return render(request, 'myapp/aprovado.html')


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('/')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'myapp/cadastro.html', {'form_usuario': form_usuario})