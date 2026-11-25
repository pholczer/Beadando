import os

import openpyxl
from openpyxl.workbook import Workbook

from data.alap.generalo import adathalmaz_generalasa
from data.alap.kezelok import csv_szotar, sajat_json, xlsx
from data.alap.modell_adatosztalyok import Szemely, Csapat, Verseny, FAJLNEVEK

DARAB = 30
MAPPA = "eredmeny"

szemelyek, csapatok, versenyek = adathalmaz_generalasa(DARAB)
adatok = {Szemely: szemelyek, Csapat: csapatok, Verseny: versenyek}
print("Legenerálva:", len(szemelyek), "kerékpáros,", len(csapatok), "csapat,", len(versenyek), "verseny")

os.makedirs(MAPPA, exist_ok=True)
munkafuzet = Workbook()
munkafuzet.remove(munkafuzet.active)
for tipus, lista in adatok.items():
    csv_szotar.ir(lista, MAPPA, FAJLNEVEK[tipus])
    sajat_json.ir(lista, MAPPA, FAJLNEVEK[tipus])
    xlsx.ir(lista, munkafuzet, FAJLNEVEK[tipus])
EXCEL_FAJL = os.path.join(MAPPA, "kerekparosok.xlsx")
munkafuzet.save(EXCEL_FAJL)
print("Az Excel fájl itt van:", os.path.abspath(EXCEL_FAJL))

munkafuzet = openpyxl.load_workbook(EXCEL_FAJL)
for tipus, lista in adatok.items():
    nev = FAJLNEVEK[tipus]
    print(nev, "- CSV:", csv_szotar.olvas(tipus, MAPPA, nev) == lista,
          "JSON:", sajat_json.olvas(tipus, MAPPA, nev) == lista,
          "Excel:", xlsx.olvas(tipus, munkafuzet, nev) == lista)

if hasattr(os, "startfile"):
    os.startfile(EXCEL_FAJL)
