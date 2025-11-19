from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='avatars/',
        default='avatars/default.png',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username

    def get_avatar_url(self):
        if self.avatar and hasattr(self.avatar, "url") and "default.png" not in self.avatar.url:
            return self.avatar.url
        return "/static/img/default.png"
