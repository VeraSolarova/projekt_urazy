from django.shortcuts import render
from urazy.models import Vek, Pohlavi, Zpusob, Zpusob_popis
import matplotlib.pyplot as plt
import io
import base64
import matplotlib.cm as cm

def index(request):
    kategorie = [
        {"nazev": "Dle věku", "url_name": "vek"},
        {"nazev": "Dle pohlaví", "url_name": "pohlavi"},
        {"nazev": "Dle způsobu", "url_name": "zpusob"},
        {"nazev": "pokus", "url_name": "pokus"},
    ]
    return render(request, 'urazy/index.html', {"kategorie": kategorie})

def graf(roky, kategorie2, vsechny_hodnoty, nadpis_grafu: str, nadpis_legendy: str, unikatni_atribut):
    fig, ax = plt.subplots(figsize=(12, 8))
    sirka_sloupce = 0.8 / len(kategorie2)
    pozice = range(len(roky))

    colormap = cm.get_cmap("tab20") 
    barvy = [colormap(i / len(kategorie2)) for i in range(len(kategorie2))]

    for i, hodnoty in enumerate(vsechny_hodnoty):
        ax.bar(
            [pos + i * sirka_sloupce for pos in pozice],
            hodnoty,
            sirka_sloupce,
            label=kategorie2[i][unikatni_atribut],  
            color=barvy[i % len(barvy)]
        )

    ax.set_xlabel("Roky")
    ax.set_ylabel("Počet úrazů")
    ax.set_xticks([pos + sirka_sloupce * len(kategorie2) / 2 for pos in pozice])
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


def vek(request):
    data = Vek.objects.filter(rok__gte=2015, rok__lte=2022)  
    roky = list(data.values_list('rok', flat=True).distinct().order_by('rok')) 
    kategorie = list(data.values_list('vek', flat=True).distinct()) 
    
    # Příprava dat pro graf
    kategorie2 = data.values("vek").distinct()  
    vsechny_hodnoty = []

    for i, skupina in enumerate(kategorie2):
        hodnoty = []
        for rok in roky:
            pocet = data.filter(rok=rok, vek=skupina['vek'])
            pocet = pocet.values_list('pocet', flat=True).first()
            
            if pocet is None:
                pocet = 0
            
            hodnoty.append(pocet)
        
        vsechny_hodnoty.append(hodnoty)

    obrazek_grafu = graf(roky, kategorie2, vsechny_hodnoty, "Graf podle veku", "Vekove kategorie", "vek")

    context = {
        'data': data,
        'roky': roky,  
        'kategorie': kategorie,  
        'obrazek_grafu': obrazek_grafu,
    }

    return render(request, "urazy/vek.html", context)


def pohlavi(request):
    
    data = Pohlavi.objects.filter(rok__gte=2015, rok__lte=2022)
    roky = data.values_list('rok', flat=True).distinct().order_by('rok')
    kategorie = Pohlavi.objects.values('pohlavi').distinct()  

    kategorie2 = data.values("pohlavi").distinct()  
    vsechny_hodnoty = []
         
    for i, skupina in enumerate(kategorie2):
        hodnoty = []
        for rok in roky:
            pocet = data.filter(rok=rok, pohlavi=skupina['pohlavi'])
            pocet = pocet.values_list('pocet', flat=True).first()
            
            if pocet is None:
                pocet = 0
            
            hodnoty.append(pocet)
        
        vsechny_hodnoty.append(hodnoty)

    obrazek_grafu = graf(roky, kategorie2, vsechny_hodnoty, "Graf podle pohlaví", "Pohlaví", "pohlavi")
    
    context = {
        'data': data,
        'roky': roky,  
        'kategorie': kategorie,  
        'obrazek_grafu': obrazek_grafu,
    }

    return render(request, "urazy/pohlavi.html", context)



def zpusob(request):
    #data = Zpusob.objects.all()
    data = Zpusob.objects.filter(rok__gte=2015, rok__lte=2022)
    roky = data.values_list('rok', flat=True).distinct().order_by('rok')   
    kategorie = data.values("zpusob").distinct()
    for kat in kategorie:
        kat["label"] = Zpusob_popis(kat["zpusob"]).label
        kat["index"] = index 


    kategorie2 = []
    for kat in kategorie:
        kategorie2.append({
            "zpusob": kat["zpusob"],
            "label": Zpusob_popis(kat["zpusob"]).label  
        })

    vsechny_hodnoty = []
         
    for i, skupina in enumerate(kategorie2):
        hodnoty = []
        for rok in roky:
            pocet = data.filter(rok=rok, zpusob=skupina['zpusob'])
            pocet = pocet.values_list('pocet', flat=True).first()
            
            if pocet is None:
                pocet = 0
            
            hodnoty.append(pocet)
        
        vsechny_hodnoty.append(hodnoty)

    context_data = []
    for skupina, hodnoty in zip(kategorie, vsechny_hodnoty):
        context_data.append({"zpusob": skupina["label"], "hodnoty": hodnoty})


    obrazek_grafu = graf(roky, kategorie2, vsechny_hodnoty, "Graf četnosti dle způsobu vzniku úrazu", "Způsoby", "label")
    
    context = {
        'data': data,
        'roky': roky,  
        'kategorie': context_data,
        'kategorie2': kategorie2,
        'obrazek_grafu': obrazek_grafu,
        'vsechny_hodnoty': vsechny_hodnoty,
    }

    return render(request, "urazy/zpusob.html", context)
