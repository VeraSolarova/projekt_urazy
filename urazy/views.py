from django.shortcuts import render
from urazy.models import Vek, Pohlavi, Zpusob
import matplotlib.pyplot as plt
import io
import base64

def index(request):
    kategorie = [
        {"nazev": "Dle věku", "url_name": "vek"},
        {"nazev": "Dle pohlaví", "url_name": "pohlavi"},
        {"nazev": "Dle způsobu", "url_name": "zpusob"},
    ]
    return render(request, 'urazy/index.html', {"kategorie": kategorie})

def vek(request):
    # Příprava dat pro tabulku
    data = Vek.objects.all()   #(všechna data - trida Vek ma atributy vek, rok, pocet )

    # Unikátní roky a věkové kategorie
    roky = data.values_list('rok', flat=True).distinct().order_by('rok') #všechny unikátní roky
    kategorie = Vek.objects.values('vek').distinct()
    
    # Příprava dat pro graf
    data_podle_roku = {rok: {item.vek: item.pocet for item in data.filter(rok=rok)} for rok in roky} 
        #složený dictionary. Vnější klíč = rok: jeho hodnotou je opět dictionary 
        # věková kategorie item.vek:(vnitřní klíč) a jeho hodnotou jsou počty úrazů item.pocet
         
    roky_graf = list(roky)
    kategorie_graf = list(data.values_list('vek', flat=True).distinct())

    # Vykreslení grafu
    fig, ax = plt.subplots(figsize=(12, 8))
    sirka_sloupce = 0.8 / len(kategorie)
    pozice = range(len(roky))

    barvy = [
        (0.7, 0.0, 0.0),  # Tlumená červená
        (0.8, 0.4, 0.0),  # Oranžová
        (0.9, 0.9, 0.0),  # Žlutá
        (0.0, 0.7, 0.0),  # Zelená
        (0.0, 0.5, 0.7),  # Světle modrá
        (0.0, 0.0, 1.0),  # Modrá
        (0.5, 0.0, 0.5),  # Fialová
        (0.6, 0.6, 0.6),  # Šedá
        (0.9, 0.6, 0.7),  # Světle růžová
        (0.3, 0.3, 0.8),  # Tlumená levandulová
        (0.5, 0.6, 0.7),  # Světle tyrkysová
    ]

    for i, skupina in enumerate(kategorie_graf):
        hodnoty = [data_podle_roku[rok].get(skupina, 0) for rok in roky_graf]
        ax.bar(
            [pos + i * sirka_sloupce for pos in pozice],
            hodnoty,
            sirka_sloupce,
            label=skupina,
            color=barvy[i % len(barvy)]
        )

    # Nastavení os a popisků
    ax.set_xlabel("Roky")
    ax.set_ylabel("Počet úrazů")
    ax.set_xticks([pos + sirka_sloupce * len(kategorie_graf) / 2 for pos in pozice])
    ax.set_xticklabels(roky_graf)
    ax.set_title("Počet úrazů dle věkových kategorií")
    ax.legend(title="Věkové kategorie")

    # Uložení grafu do obrázku
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    obrazek_grafu = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()


    context = {
        'data': data,
        'roky': roky,  
        'kategorie': kategorie,  
        'obrazek_grafu': obrazek_grafu,  
    }

    return render(request, "urazy/vek.html", context)










def pohlavi(request):
    
    data = Pohlavi.objects.all()
    roky = data.values_list('rok', flat=True).distinct().order_by('rok')
    kategorie = Pohlavi.objects.values('pohlavi').distinct()  

    # Příprava dat pro graf
    data_podle_roku = {rok: {item.pohlavi: item.pocet for item in data.filter(rok=rok)} for rok in roky} 
        #složený dictionary. Vnější klíč = rok: jeho hodnotou je opět dictionary 
        # věková kategorie item.vek:(vnitřní klíč) a jeho hodnotou jsou počty úrazů item.pocet
         
    roky_graf = list(roky)
    kategorie_graf = list(data.values_list('pohlavi', flat=True).distinct())

    # Vykreslení grafu
    fig, ax = plt.subplots(figsize=(12, 8))
    sirka_sloupce = 0.8 / len(kategorie)
    pozice = range(len(roky))

    barvy = [
        (0.7, 0.0, 0.0),  # Tlumená červená
        (0.8, 0.4, 0.0),  # Oranžová
        (0.9, 0.9, 0.0),  # Žlutá
        (0.0, 0.7, 0.0),  # Zelená
        (0.0, 0.5, 0.7),  # Světle modrá
        (0.0, 0.0, 1.0),  # Modrá
        (0.5, 0.0, 0.5),  # Fialová
        (0.6, 0.6, 0.6),  # Šedá
        (0.9, 0.6, 0.7),  # Světle růžová
        (0.3, 0.3, 0.8),  # Tlumená levandulová
        (0.5, 0.6, 0.7),  # Světle tyrkysová
    ]

    for i, skupina in enumerate(kategorie_graf):
        hodnoty = [data_podle_roku[rok].get(skupina, 0) for rok in roky_graf]
        ax.bar(
            [pos + i * sirka_sloupce for pos in pozice],
            hodnoty,
            sirka_sloupce,
            label=skupina,
            color=barvy[i % len(barvy)]
        )

    # Nastavení os a popisků
    ax.set_xlabel("Roky")
    ax.set_ylabel("Počet úrazů")
    ax.set_xticks([pos + sirka_sloupce * len(kategorie_graf) / 2 for pos in pozice])
    ax.set_xticklabels(roky_graf)
    ax.set_title("Počet úrazů dle pohlaví")
    ax.legend(title="M-Muž F-žena")

    # Uložení grafu do obrázku
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    obrazek_grafu = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()


    context = {
        'data': data,
        'roky': roky,
        'kategorie': kategorie,
        'obrazek_grafu': obrazek_grafu,  
    }

    return render(request, "urazy/pohlavi.html", context)














































def zpusob(request):
    zpusob_data = Zpusob.objects.all()
    years = zpusob_data.values_list('rok', flat=True).distinct().order_by('rok')
    cause_groups = Zpusob.objects.values('zpusob').distinct()  # Získáme všechny unikátní věkové kategorie

    context = {
        'zpusob_data': zpusob_data,
        'years': years,
        'cause_groups': cause_groups,
    }

    return render(request, "urazy/zpusob.html", context)


