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
    vek_data = Vek.objects.all()
    years = vek_data.values_list('rok', flat=True).distinct().order_by('rok')
    age_groups = Vek.objects.values('vek').distinct()

    # Příprava dat pro graf
    data_by_year = {year: {item.vek: item.pocet for item in vek_data.filter(rok=year)} for year in years}
    years = list(years)
    age_groups = [group['vek'] for group in age_groups]

    # Vykreslení grafu
    fig, ax = plt.subplots(figsize=(12, 8))
    bar_width = 0.8/len(age_groups)
    x = range(len(years))

    colors = [
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

    for i, age_group in enumerate(age_groups):
        values = [data_by_year[year].get(age_group, 0) for year in years]
        ax.bar(
            [pos + i * bar_width for pos in x],
            values,
            bar_width,
            label=age_group,
            color=colors[i % len(colors)]
        )

    # Nastavení os a popisků
    ax.set_xlabel("Rok")
    ax.set_ylabel("Počet")
    ax.set_xticks([pos + bar_width * len(age_groups) / 2 for pos in x])
    ax.set_xticklabels(years)
    ax.set_title("Počet věkových skupin za roky")
    ax.legend()

    # Uložení grafu do obrázku
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph_url = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    context = {
        'vek_data': vek_data,
        'years': years,
        'age_groups': age_groups,
        'graph_url': graph_url,
    }

    return render(request, "urazy/vek.html", context)

def pohlavi(request):
    pohlavi_data = Pohlavi.objects.all()
    years = pohlavi_data.values_list('rok', flat=True).distinct().order_by('rok')
    gender_groups = Pohlavi.objects.values('pohlavi').distinct()

    context = {
        'pohlavi_data': pohlavi_data,
        'years': years,
        'gender_groups': gender_groups,
    }

    return render(request, "urazy/pohlavi.html", context)


def zpusob(request):
    zpusob_data = Zpusob.objects.all()
    years = zpusob_data.values_list('rok', flat=True).distinct().order_by('rok')
    cause_groups = Zpusob.objects.values('zpusob').distinct()

    context = {
        'zpusob_data': zpusob_data,
        'years': years,
        'cause_groups': cause_groups,
    }

    return render(request, "urazy/zpusob.html", context)
