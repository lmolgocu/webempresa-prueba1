from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = QuillField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de Creación")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de Edición")

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ["order", "title"]

    def __str__(self):
        return self.title