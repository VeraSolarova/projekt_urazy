from django.db import models
import pandas as pd


# Create your models here.

# agregovana data úrazů:  Počty za jednotivé roky přepočtené na 100 000 obyvatel ČR, kategorie, pohlaví, věku nebo regionu



class Pohlavi(models.Model):
    pohlavi = models.CharField(max_length=4) # Muži, Ženy
    rok = models.IntegerField(null=True, blank=True, default=None)
    pocet = models.IntegerField(null=True, blank=True, default=None)  

    def __str__(self):
        return f"{self.pohlavi}: {self.rok}"

class Vek(models.Model):
    vek = models.CharField(max_length=10) # 10-19, 20-29
    rok = models.IntegerField(null=True, blank=True, default=None)
    pocet = models.IntegerField(null=True, blank=True, default=None)   
    
    def __str__(self):
        return f"věk: {self.vek}: {self.rok}"
    
