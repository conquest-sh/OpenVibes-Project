from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Overall(models.Model):
    name = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    

class Individaul(models.Model):
    name = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Explain(models.Model):
    esm = models.ForeignKey(Overall, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..."
    
class Explain2(models.Model):
    esmm = models.ForeignKey(Individaul, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    