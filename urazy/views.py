from django.shortcuts import render
from urazy.models import Vek, Pohlavi, Zpusob
import matplotlib.pyplot as plt
import io
import base64
from django.db.models.query import QuerySet


def index(request):
    kategorie = [
        {"nazev": "Dle věku", "url_name": "vek"},
        {"nazev": "Dle pohlaví", "url_name": "pohlavi"},
        {"nazev": "Dle způsobu", "url_name": "zpusob"},
        {"nazev": "pokus", "url_name": "pokus"},
    ]
    return render(request, 'urazy/index.html', {"kategorie": kategorie})

def vek(request):
    # Příprava dat pro tabulku
    data = Vek.objects.all()   #(všechna data - trida Vek ma atributy vek, rok, pocet )
    roky = list(data.values_list('rok', flat=True).distinct().order_by('rok')) #všechny unikátní roky
    kategorie = list(data.values_list('vek', flat=True).distinct()) #
    
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

    # Cyklus přes všechny kategorie (věkové kategorie)
    for i, skupina in enumerate(kategorie):
        # Vytvoření seznamu hodnot pro danou kategorii a rok
        hodnoty = []
        
        # Pro každý rok zjistíme hodnoty pro danou kategorii
        for rok in roky:
            # Filtrace dat pro tento rok a kategorii
            
            pocet = data.filter(rok=rok, vek=skupina).values_list('pocet', flat=True).first()
            
            # Pokud není žádný záznam pro tento rok a kategorii, použijeme 0
            if pocet is None:
                pocet = 0
                
            hodnoty.append(pocet)

        # Vykreslení sloupcového grafu pro danou kategorii
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
    ax.set_xticks([pos + sirka_sloupce * len(kategorie) / 2 for pos in pozice])
    ax.set_xticklabels(roky)
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
































def pokus_tabulka(data: QuerySet, objekt: type, unikatni_atribut: str):
    roky = list(data.values_list('rok', flat=True).distinct().order_by('rok'))  # unikátní roky [2019,2020,...]   
    kategorie = objekt.objects.values(unikatni_atribut).distinct()  # např. list pohlaví [F, M]
    return roky, kategorie

def pokus_graf(roky, data: QuerySet, kategorie, vsechny_hodnoty, nadpis_grafu: str, nadpis_legendy: str, unikatni_atribut):
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

    for i, hodnoty in enumerate(vsechny_hodnoty):
        ax.bar(
            [pos + i * sirka_sloupce for pos in pozice],
            hodnoty,
            sirka_sloupce,
            label=kategorie[i][unikatni_atribut],  # Oprava pro přístup k hodnotě 'vek', 'pohlavi', atd.
            color=barvy[i % len(barvy)]
        )

    ax.set_xlabel("Roky")
    ax.set_ylabel("Počet úrazů")
    ax.set_xticks([pos + sirka_sloupce * len(kategorie) / 2 for pos in pozice])
    ax.set_xticklabels(roky)
    ax.set_title(nadpis_grafu)
    ax.legend(title=nadpis_legendy)

    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    obrazek_grafu = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    return obrazek_grafu

def pokus(request):

    data = Vek.objects.all()
    roky, kategorie = pokus_tabulka(data, Vek, "vek")
    

    vsechny_hodnoty = []

    for i, skupina in enumerate(kategorie):
        hodnoty = []
        for rok in roky:
            # Opravená filtrace podle 'vek' a hodnoty z 'skupina'
            pocet = data.filter(rok=rok, vek=skupina['vek'])
            pocet = pocet.values_list('pocet', flat=True).first()
            
            if pocet is None:
                pocet = 0
            
            hodnoty.append(pocet)
        
        vsechny_hodnoty.append(hodnoty)

    obrazek_grafu = pokus_graf(roky, data, kategorie, vsechny_hodnoty, "Graf podle veku", "Vekove kategorie", "vek")

    context = {
        'data': data,
        'roky': roky,
        'kategorie': kategorie,
        'obrazek_grafu': obrazek_grafu,
    }

    return render(request, "urazy/pokus.html", context)



























































































































































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


