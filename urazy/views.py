from django.shortcuts import render, get_object_or_404
from urazy.models import Vek, Pohlavi



# Create your views here.

def urazy_uvod(request):
    vsechny_veky = Vek.objects.all() # django dyntaxe pro databazove dotazy
    vsechna_pohlavi = Pohlavi.objects.all()
    context = {'vek': vsechny_veky, 'pohlavi': vsechna_pohlavi}
    return render(request, 'urazy/urazy_uvod.html', context)

def urazy_data(request):
    # Načtení všech dat, pokud není potřeba filtrovat podle pk
    pohlavi_data = Pohlavi.objects.all()  # Načti všechna pohlaví
    vek_data = Vek.objects.all()  # Načti všechny věkové kategorie

    # Připravený kontext
    context = {
        "pohlavi_data": pohlavi_data,
        "vek_data": vek_data,
    }
    return render(request, "urazy/urazy_data.html", context)