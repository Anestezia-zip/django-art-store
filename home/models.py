from django.db import models

class PaintingRequest(models.Model):
    description = models.TextField(verbose_name='Description of the painting')
    size = models.CharField(max_length=20, verbose_name='Size of the painting')
    custom_size = models.CharField(max_length=50, blank=True, null=True, verbose_name='Custom size', help_text='Specify the size if not in the list')
    add_signature = models.BooleanField(default=True, verbose_name='Add artist signature')
    examples = models.FileField(upload_to='painting_examples/', verbose_name='File with examples', blank=True, null=True)

    def __str__(self):
        return self.description
