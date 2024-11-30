from django.urls import reverse

def kategorie_context(request):
    navigation_links = [
        {'name': 'Domů', 'url': reverse('index')},
        {'name': 'Věk', 'url': reverse('vek')},
        {'name': 'Pohlaví', 'url': reverse('pohlavi')},
        {'name': 'Způsob', 'url': reverse('zpusob')},
        {'name': 'Graf věku', 'url': reverse('urazy_graf')},
    ]
    return {
        'navigation_links': navigation_links,
    }