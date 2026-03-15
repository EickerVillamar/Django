
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm
from django.core.paginator import Paginator

def inicio(request):
    return HttpResponse("Hola, estás entrando a tu primer proyecto Django")

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Producto


def lista_productos(request):
    query = request.GET.get("q")
    orden = request.GET.get("orden")
    productos_list = Producto.objects.all()
    if query:
        productos_list = productos_list.filter(nombre__icontains=query)

    if orden:
        productos_list = productos_list.order_by(orden)

    paginator = Paginator(productos_list, 5)
    page_number = request.GET.get("page")
    productos = paginator.get_page(page_number)
    return render(request, "core/productos.html", {"productos": productos})


def crear_producto(request):

    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos")
    else:
        form = ProductoForm()
    return render(request, "core/crear_producto.html", {"form": form})



def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)      #Este formulario está vinculado al objeto
        if form.is_valid():
            form.save()
            return redirect("productos")
    else:
        form = ProductoForm(instance=producto)
    return render(request, "core/editar_producto.html", {"form": form})



def eliminar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        producto.delete()
        return redirect("productos")

    return render(request, "core/eliminar_producto.html", {"producto": producto})






"""from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages


def inicio(request):
    return HttpResponse("Hola, estás entrando a tu primer proyecto Django")

class ProductoListView(ListView):
    model = Producto
    template_name = "core/productos.html"
    context_object_name = "productos"
    
    def get_queryset(self):

        query = self.request.GET.get("q")

        if query:
            return Producto.objects.filter(nombre__icontains=query)

        return Producto.objects.all()


class ProductoCreateView(CreateView):

    model = Producto
    form_class = ProductoForm
    template_name = "core/crear_producto.html"
    success_url = reverse_lazy("productos")
   
    def form_valid(self, form):
        messages.success(self.request, "Producto creado correctamente")
        return super().form_valid(form)



class ProductoUpdateView(UpdateView):

    model = Producto
    form_class = ProductoForm
    template_name = "core/editar_producto.html"
    success_url = reverse_lazy("productos")
    
    def form_valid(self, form):
        messages.success(self.request, "Producto actualizado correctamente")
        return super().form_valid(form)



class ProductoDeleteView(DeleteView):

    model = Producto
    template_name = "core/eliminar_producto.html"
    success_url = reverse_lazy("productos")
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Producto eliminado correctamente")
        return super().delete(request, *args, **kwargs)
"""