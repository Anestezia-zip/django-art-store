from django.db import models

class PaintingRequest(models.Model):
    email = models.EmailField(verbose_name='Email', default="")
    description = models.TextField(verbose_name='Description of the painting')
    size = models.CharField(max_length=20, verbose_name='Size of the painting')
    add_signature = models.BooleanField(default=True, verbose_name='Add artist signature')
    examples = models.ImageField(upload_to='painting_examples/', verbose_name='Files with examples:', blank=True, null=True)
    examples2 = models.ImageField(upload_to='painting_examples/', verbose_name='', blank=True, null=True)

    def __str__(self):
        return self.description


class TemporaryPaintingRequest(models.Model):
    email = models.EmailField()
    description = models.TextField(verbose_name='Description of the painting', default="")
    size = models.CharField(max_length=20, verbose_name='Size of the painting', default="")
    add_signature = models.BooleanField(default=True, verbose_name='Add artist signature')
    examples = models.ImageField(upload_to='painting_examples/', verbose_name='Files with examples:', blank=True, null=True)
    examples2 = models.ImageField(upload_to='painting_examples/', verbose_name='', blank=True, null=True)

    def __str__(self):
        return self.description