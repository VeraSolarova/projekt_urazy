from django.contrib import admin

# username: username 
# password: hesloheslo


# Register your models here.
from urazy import models #všechny modely importuji 
from urazy.models import Vek, Pohlavi, Zpusob  # Import modelu Vek

#admin.site.register(models.Vek) #námi vytvořený model přidáme do admin sekce  
#admin.site.register(models.Pohlavi)



# Registrace modelu Vek v Django Admin
class VekAdmin(admin.ModelAdmin):
    # Definování polí, která se zobrazí v přehledu záznamů
    list_display = ('id', 'vek', 'rok', 'pocet' )  # Ujistěte se, že chcete zobrazit pole 'rok'
    search_fields = ('vek', 'rok', 'pocet')  # Možnost vyhledávání podle věku

admin.site.register(Vek, VekAdmin)

class PohlaviAdmin(admin.ModelAdmin):
    # Definování polí, která se zobrazí v přehledu záznamů
    list_display = ('id', 'pohlavi', 'rok', 'pocet' )  # Ujistěte se, že chcete zobrazit pole 'rok'
    search_fields = ('pohlavi', 'rok', 'pocet')  # Možnost vyhledávání podle věku

admin.site.register(Pohlavi, PohlaviAdmin)

class ZpusobAdmin(admin.ModelAdmin):
    # Definování polí, která se zobrazí v přehledu záznamů
    list_display = ('id', 'zpusob', 'rok', 'pocet' )  # Ujistěte se, že chcete zobrazit pole 'rok'
    search_fields = ('zpusob', 'rok', 'pocet')  # Možnost vyhledávání podle věku

admin.site.register(Zpusob, ZpusobAdmin)