from django import forms
from .models import Product, Comment

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 'price', 'image', 'category', 'stock', "active"]
        labels = {
            'name': 'Nombre del producto',
            'description': 'Descripción',
            'brand': 'Marca',
            'price': 'Precio',
            "stock": "Stock disponible",
            'image': 'Agregar imagen',
            'category': 'Categoría',
            'active': 'Activo',
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # ejemplo: limitar tamaño a 5 MB
            max_mb = 5
            if image.size > max_mb * 1024 * 1024:
                raise forms.ValidationError(f"El archivo supera las {max_mb} MB.")
            # posible validación de tipo:
            # if not image.content_type.startswith('image/'):
            #     raise forms.ValidationError("Subí una imagen válida.")
        return image


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Escribe tu comentario..."
            }),
        }
