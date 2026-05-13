from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )
    tipo_usuario = models.CharField(
        max_length=30,
        choices=TIPO_USUARIO,
        blank=True,
        default='',
    )

    def __str__(self):
        return f'{self.username} ({self.get_tipo_usuario_display()})'


class Professor(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name='professor',
    )
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return f'Prof. {self.usuario.get_full_name() or self.usuario.username}'


class Aluno(models.Model):
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name='aluno',
    )

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username


