from django.db import models


class Music(models.Model):
    mus_file = models.FileField(upload_to='music_files/%Y/%m/%d/')
    title = models.CharField(max_length=150, verbose_name='Название')
    text = models.TextField(blank=True, verbose_name='Текст песни')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыки'
        ordering = ['-created_at']

# Create your models here.
