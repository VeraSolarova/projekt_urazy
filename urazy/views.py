from django.shortcuts import render, get_object_or_404
from urazy.models import Vek, Pohlavi, Zpusob


"""def index(request):
    vek = Vek.objects.all() # django dyntaxe pro databazove dotazy
    pohlavi = Pohlavi.objects.all()
    context = {'vek': vek, 'pohlavi': pohlavi}

    return render(request, 'urazy/index.html', context)"""

def index(request):
    kategorie = [
        {"nazev": "Dle věku", "url_name": "vek"},
        {"nazev": "Dle pohlaví", "url_name": "pohlavi"},
        {"nazev": "Dle způsobu", "url_name": "zpusob"},
    ]
    return render(request, 'urazy/index.html', {"kategorie": kategorie})

def vek(request):
    # Načteme všechna data
    vek_data = Vek.objects.all()

    # Shromáždíme všechny unikátní roky
    years = vek_data.values_list('rok', flat=True).distinct().order_by('rok')

    # Shromáždíme data pro každou věkovou kategorii
    age_groups = Vek.objects.values('vek').distinct()  # Získáme všechny unikátní věkové kategorie

    context = {
        'vek_data': vek_data,
        'years': years,
        'age_groups': age_groups,
    }

    return render(request, "urazy/vek.html", context)

def pohlavi(request):
    # Načteme všechna data
    pohlavi_data = Pohlavi.objects.all()

    # Shromáždíme všechny unikátní roky
    years = pohlavi_data.values_list('rok', flat=True).distinct().order_by('rok')

    # Shromáždíme data pro každou věkovou kategorii
    gender_groups = Pohlavi.objects.values('pohlavi').distinct()  # Získáme všechny unikátní věkové kategorie

    context = {
        'pohlavi_data': pohlavi_data,
        'years': years,
        'gender_groups': gender_groups,
    }

    return render(request, "urazy/pohlavi.html", context)


def zpusob(request):
    # Načteme všechna data
    zpusob_data = Zpusob.objects.all()

    # Shromáždíme všechny unikátní roky
    years = zpusob_data.values_list('rok', flat=True).distinct().order_by('rok')

    # Shromáždíme data pro každou věkovou kategorii
    cause_groups = Pohlavi.objects.values('zpusob').distinct()  # Získáme všechny unikátní věkové kategorie

    context = {
        'zpusob_data': zpusob_data,
        'years': years,
        'cause_groups': cause_groups,
    }

    return render(request, "urazy/zpusob.html", context)


def vek_graf(request):
    # Získání dat
    vek_data = Vek.objects.all()

    # Unikátní roky a věkové skupiny
    years = sorted(vek_data.values_list('rok', flat=True).distinct())
    age_groups = vek_data.values_list('vek', flat=True).distinct()

    # Generování části URL pro štítky (labels)
    labels = ",".join([f"'{year}'" for year in years])

    # Generování datových sad (datasets)
    datasets = []
    for vek in age_groups:
        data = []
        for rok in years:
            count = vek_data.filter(vek=vek, rok=rok).first()
            data.append(count.pocet if count else 0)
        data_values = ",".join(map(str, data))
        datasets.append(f"{{label:'{vek}',data:[{data_values}]}}")

    datasets_str = ",".join(datasets)

    # Sestavení URL
    chart_url = (
        "https://quickchart.io/chart?width=1000&height=500&chart="
        f"{{type:'bar',data:{{labels:[{labels}],datasets:[{datasets_str}]}}}}"
    )

    return render(request, 'urazy/vek_graf.html', {
        "chart_url": chart_url,
        "years": years,
        "vek_data": vek_data
    })