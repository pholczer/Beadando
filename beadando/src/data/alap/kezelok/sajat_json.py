import json
import os
from dataclasses import asdict

from data.alap.modell_adatosztalyok import sorbol_objektum


def ir(lista: list, mappa: str, fajl_nev: str) -> None:
    with open(os.path.join(mappa, fajl_nev + ".json"), "w", encoding="utf-8") as fajl:
        json.dump([asdict(elem) for elem in lista], fajl, indent=2, ensure_ascii=False)


def olvas(tipus, mappa: str, fajl_nev: str) -> list:
    with open(os.path.join(mappa, fajl_nev + ".json"), "r", encoding="utf-8") as fajl:
        return [sorbol_objektum(tipus, dokumentum) for dokumentum in json.load(fajl)]
