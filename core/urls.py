
from django.urls import path
from .views import inicio, lista_productos, crear_producto, editar_producto, eliminar_producto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('productos/',lista_productos, name='productos'),
    path('crear-producto/',crear_producto, name='crear-producto'),
    path("editar-producto/<int:id>/", editar_producto, name="editar_producto"),
    path("eliminar-producto/<int:id>/", eliminar_producto, name="eliminar_producto"),
]



"""
from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    inicio
)

urlpatterns = [
    path("",inicio,name="inicio"),

    path("productos/", ProductoListView.as_view(), name="productos"),

    path("crear-producto/", ProductoCreateView.as_view(), name="crear_producto"),

    path("editar-producto/<int:pk>/", ProductoUpdateView.as_view(), name="editar_producto"),

    path("eliminar-producto/<int:pk>/", ProductoDeleteView.as_view(), name="eliminar_producto"),
]

"""