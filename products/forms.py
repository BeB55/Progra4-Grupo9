from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["user",'nombre', 'precio', 'descripcion']

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