from django.db import models

class OrigWord(models.Model):

    name = models.CharField(max_length=20, help_text='Non-academic word')
    replacement = models.ManyToManyField('Replacement')

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.name

class Replacement(models.Model):

    name = models.CharField(max_length=50, help_text='to be replaced with')

    def __str__(self):
        return self.name