from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

# Create your views here.


def index(request):
    return HttpResponse("Olá mundo.")


def listar(request):
    produto = Produto.objects.all()
    return render(request, "listar.html", {"produto": produto})


def cadastrar(request):
    if request.method == "GET":
        status = request.GET.get("status")
        return render(request, "cadastrar.html", {"status": status})
    elif request.method == "POST":
        produto = request.POST.get("Produto")
        preco = request.POST.get("Preco")
        modelProd = Produto(
            produto=produto,
            preco=preco
        )
        modelProd.save()
        return redirect("/produtos/cadastrar?status=1")


def alterar(request):
    return HttpResponse("Alterar")


def excluir(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect("/produtos/listar")
