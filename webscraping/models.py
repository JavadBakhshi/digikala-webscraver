from django.db import models

class Scrape(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Scrape"
        
        
    def __str__(self):
        return self.title
    
    
