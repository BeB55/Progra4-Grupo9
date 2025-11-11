from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

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