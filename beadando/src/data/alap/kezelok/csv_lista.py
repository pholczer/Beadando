import csv
import os
from dataclasses import astuple

from data.alap.modell_adatosztalyok import mezonevek, sorbol_objektum


def ir(lista: list, mappa: str, fajl_nev: str, elvalaszto: str = ";") -> None:
    with open(os.path.join(mappa, fajl_nev + ".csv"), "w", newline="", encoding="utf-8-sig") as fajl:
        iro = csv.writer(fajl, delimiter=elvalaszto)
        iro.writerow(mezonevek(type(lista[0])))
        for elem in lista:
            iro.writerow(astuple(elem))


def olvas(tipus, mappa: str, fajl_nev: str, elvalaszto: str = ";") -> list:
    with open(os.path.join(mappa, fajl_nev + ".csv"), "r", newline="", encoding="utf-8-sig") as fajl:
        olvaso = csv.reader(fajl, delimiter=elvalaszto)
        fejlec = next(olvaso)
        return [sorbol_objektum(tipus, dict(zip(fejlec, sor))) for sor in olvaso]
