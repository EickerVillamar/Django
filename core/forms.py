""""
Con esto de aquí le estamos diciendo a DJango, "Crea un formulario basado en el modelo Producto
Entonces Django genera inputs para los diferentes campos
"""""

from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ["nombre", "precio", "stock"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2 shadow-sm focus:ring-blue-500 focus:border-blue-500'}),
            'precio': forms.NumberInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2 shadow-sm'}),
            'stock': forms.NumberInput(attrs={'class': 'mt-1 block w-full border border-gray-300 rounded-md p-2 shadow-sm'}),
        }
    