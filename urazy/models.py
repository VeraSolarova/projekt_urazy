from django.db import models

#PS C:\Users\Student\python\projekt_urazy> pip freeze > r.txt  -ulozi vsechny pouzite knihovny to textoveho soubru
#PS C:\Users\Student\python\projekt_urazy> pip install -r r.txt  - naistaluje vsehny ppouzite knihovny ze souboru txt

# agregovana data úrazů:  Počty za jednotivé roky přepočtené na 100 000 obyvatel ČR, kategorie, pohlaví, věku nebo regionu

class Pohlavi(models.Model):
    pohlavi = models.CharField(max_length=4)
    rok = models.IntegerField(null=True, blank=True, default=None)
    pocet = models.IntegerField(null=True, blank=True, default=None)  

    def __str__(self):
        return f"{self.pohlavi}: {self.rok}"

class Vek(models.Model):
    vek = models.CharField(max_length=10) 
    rok = models.IntegerField(null=True, blank=True, default=None)
    pocet = models.IntegerField(null=True, blank=True, default=None)   
    
    def __str__(self):
        return f"věk: {self.vek}: {self.rok}"
    
class Zpusob(models.Model):
    zpusob = models.CharField(max_length=7)  
    rok = models.IntegerField(null=True, blank=True, default=None)
    pocet = models.IntegerField(null=True, blank=True, default=None)   
    
    def __str__(self):
        return f"způsob: {self.zpusob}: {self.rok}"
    

