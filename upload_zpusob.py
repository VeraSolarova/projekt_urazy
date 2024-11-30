import os
import django

# Nastavení proměnné prostředí pro Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_project.settings')

# Inicializace Django
django.setup()

import pandas as pd
from urazy.models import Zpusob


file_path = 'zpusob.xlsx'
data = pd.read_excel(file_path, index_col=0)  # index_col=0 - první sloupec vekove kategorie bude "index"

for zpusob, row in data.iterrows(): # data.iterrows() je metoda pandas iteruje přes každý řádek, vek - hodnota indexu pro aktuální řádek (index_col=0)
    for rok, pocet in row.items():# row.items() je metoda, která iteruje přes všechny položky (sloupce) ve row, název sloupce - rok je klíč, pocet je hodnota pro daný rok a věkovou skupinu.
        if pd.notna(pocet):  # Ověření NaN (Not a Number) - to by byla prázdná buňka nebo neplatná hodnota
            zpusob_instance = Zpusob(
                zpusob=str(zpusob),  
                rok=int(rok),  
                pocet=int(pocet)  
            )
            zpusob_instance.save() #Funkce save() je metoda Django modelu, která ukládá objekt do databázové tabulky podle definice modelu.

print("Data byla úspěšně nahrána do databáze.")