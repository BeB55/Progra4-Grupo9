from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

from django import forms
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingresá tu contraseña'}),
        help_text=None
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Repetí tu contraseña'}),
        help_text=None
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Elimina los textos de ayuda automáticos
        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs.update({'class': 'form-control'})  # (opcional, para CSS)

class AvatarForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Evita que Django genere el checkbox "Clear"
        if hasattr(self.fields['avatar'], 'widget'):
            self.fields['avatar'].widget.clear_checkbox = False
            self.fields['avatar'].widget.template_name = 'django/forms/widgets/file.html'

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    def clean(self):
        cleaned_data = super().clean()
        user = authenticate(
            username=cleaned_data.get("username"),
            password=cleaned_data.get("password")
        )

        if not user:
            raise forms.ValidationError("Usuario o contraseña incorrectos")

        cleaned_data["user"] = user
        return cleaned_data