from django.db import models




class Maqola(models.Model):
    sarlavha=models.CharField(max_length=60)
    matn=models.TextField()
    sana=models.DateField()
    rasm=models.FileField(blank=True)
    def __str__(self):
        return self.sarlavha
class Intervyu(models.Model):
    sarlavha=models.CharField(max_length=50)
    sana=models.DateField()
    link=models.CharField(max_length=150)
    def __str__(self): return self.sarlavha