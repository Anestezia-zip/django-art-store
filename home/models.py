from django.db import models
from cloudinary.models import CloudinaryField


class PaintingRequest(models.Model):
    email = models.EmailField(verbose_name='Email', default="")
    description = models.TextField(verbose_name='Description of the painting')
    size = models.CharField(max_length=20, verbose_name='Size of the painting')
    add_signature = models.BooleanField(default=True, verbose_name='Add artist signature')
    examples = models.ImageField(upload_to='painting_examples/', verbose_name='File with examples:', blank=True, null=True)
    examples = CloudinaryField(
        'image',
        default='placeholder',
        upload_preset='art-store'
    )

    def __str__(self):
        return self.description
