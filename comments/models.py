from django.db import models

class Comment(models.Model):
    name = models.CharField("name", max_length=50 )
    comment = models.TextField(help_text='digite seu comentario', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
        
    def __str__(self):
        return self.name