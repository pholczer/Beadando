import csv
import os
from dataclasses import asdict

from data.alap.modell_adatosztalyok import mezonevek, sorbol_objektum


def ir(lista: list, mappa: str, fajl_nev: str, elvalaszto: str = ";") -> None:
    with open(os.path.join(mappa, fajl_nev + ".csv"), "w", newline="", encoding="utf-8-sig") as fajl:
        iro = csv.DictWriter(fajl, fieldnames=mezonevek(type(lista[0])), delimiter=elvalaszto)
        iro.writeheader()
        for elem in lista:
            iro.writerow(asdict(elem))


def olvas(tipus, mappa: str, fajl_nev: str, elvalaszto: str = ";") -> list:
    with open(os.path.join(mappa, fajl_nev + ".csv"), "r", newline="", encoding="utf-8-sig") as fajl:
        return [sorbol_objektum(tipus, sor) for sor in csv.DictReader(fajl, delimiter=elvalaszto)]
