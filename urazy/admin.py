from django.contrib import admin

# username: username 
# password: hesloheslo

from urazy.models import Vek, Pohlavi, Zpusob  

class VekAdmin(admin.ModelAdmin):
    list_display = ('id', 'vek', 'rok', 'pocet' )  
    search_fields = ('vek', 'rok', 'pocet')  #

admin.site.register(Vek, VekAdmin)

class PohlaviAdmin(admin.ModelAdmin):
    list_display = ('id', 'pohlavi', 'rok', 'pocet' )  
    search_fields = ('pohlavi', 'rok', 'pocet')  

admin.site.register(Pohlavi, PohlaviAdmin)

class ZpusobAdmin(admin.ModelAdmin):
    list_display = ('id', 'zpusob', 'rok', 'pocet' )  
    search_fields = ('zpusob', 'rok', 'pocet')  

admin.site.register(Zpusob, ZpusobAdmin)