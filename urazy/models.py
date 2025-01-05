from django.db import models

#PS C:\Users\Student\python\projekt_urazy> pip freeze > r.txt  -ulozi vsechny pouzite knihovny to textoveho soubru
#PS C:\Users\Student\python\projekt_urazy> pip install -r r.txt  - naistaluje vsehny ppouzite knihovny ze souboru txt

# agregovana data úrazů:  Počty za jednotivé roky přepočtené na 100 000 obyvatel ČR, kategorie, pohlaví, věku nebo regionu


class Pohlavi(models.Model):
    pohlavi = models.CharField(max_length=4) 
    rok = models.IntegerField(null=True, blank=True, default=None) 
    pocet = models.IntegerField(null=True, blank=True, default=None)   

    def __str__(self):
        return f"pohlavi: {self.pohlavi}, rok: {self.rok}, počet:{self.pocet}"

class Vek(models.Model):
    vek = models.CharField(max_length=10) # (vekove kategorie: 0-9, 10-19, neuvedeno, ..)
    rok = models.IntegerField(null=True, blank=True, default=None) # (roky: 2019, 2022, ..)
    pocet = models.IntegerField(null=True, blank=True, default=None) # (počty úrazů: 20283, 33559, ..)
    
    def __str__(self):
        return f"věk: {self.vek}, rok: {self.rok}, počet: {self.pocet}"
    
class Zpusob_popis(models.TextChoices):
    V01_V09 = "V01_V09", "Chodec zraněný při dopravní nehodě"
    V10_V19 = "V10_V19", "Cyklista zraněný při dopravní nehodě"
    V20_V29 = "V20_V29", "Jezdec na motocyklu zraněný při dopravní nehodě"
    V30_V39 = "V30_V39", "Člen osádky tříkolového motorového vozidla zraněný při dopravní nehodě"
    V40_V49 = "V40_V49", "Člen osádky osobního automobilu zraněný při dopravní nehodě"
    V50_V59 = "V50_V59", "Člen osádky dodávkového nebo lehkého nákladního automobilu zraněný při dopravní nehodě"
    V60_V69 = "V60_V69", "Člen osádky těžkého nákladního vozidla zraněný při dopravní nehodě"
    V70_V79 = "V70_V79", "Člen osádky autobusu zraněný při dopravní nehodě"
    V80_V89 = "V80_V89", "Jiné nehody při pozemní dopravě"
    V90_V94 = "V90_V94", "Nehody při vodní dopravě"
    V95_V97 = "V95_V97", "Nehody při dopravě vzduchem a vesmírným prostorem"
    V98_V99 = "V98_V99", "Jiné a neurčené dopravní nehody"
    W00_W19 = "W00_W19", "Pády"
    W20_W49 = "W20_W49", "Vystavení neživotným mechanickým silám"
    W50_W64 = "W50_W64", "Vystavení životným mechanickým silám"
    W65_W74 = "W65_W74", "Náhodné (u)tonutí a potopení"
    W75_W84 = "W75_W84", "Jiná náhodná ohrožení dýchání"
    W85_W99 = "W85_W99", "Vystavení elektrickému proudu, ozáření a extrémní okolní teplotě a tlaku vzduchu"
    X00_X09 = "X00_X09", "Vystavení kouři, ohni, dýmu a plamenů"
    X10_X19 = "X10_X19", "Kontakt s horkem a horkými látkami"
    X20_X29 = "X20_X29", "Kontakt s jedovatými živočichy a rostlinam"
    X30_X39 = "X30_X39", "Vystavení přírodním silám"
    X40_X49 = "X40_X49", "Neúmyslné sebezranění"
    X50_X57 = "X50_X57", "Úmyslné sebezranění"
    X58_X59 = "X58_X59", "Úmyslná sebevražda"

    def __str__(self):
        return self.label

class Zpusob(models.Model):
    zpusob = models.CharField(max_length=7, choices=Zpusob_popis.choices,)
    rok = models.IntegerField(null=True, blank=True, default=None)
    pocet = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        zpusob_label = Zpusob_popis(self.zpusob).label
        return f"Způsob: {zpusob_label}, rok: {self.rok}, počet:{self.pocet}"
    
    
