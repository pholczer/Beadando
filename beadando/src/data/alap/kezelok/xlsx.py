from dataclasses import astuple

from openpyxl.workbook import Workbook

from data.alap.modell_adatosztalyok import mezonevek, sorbol_objektum


def ir(lista: list, munkafuzet: Workbook, munkalap_nev: str) -> None:
    munkalap = munkafuzet.create_sheet(munkalap_nev)
    munkalap.append(mezonevek(type(lista[0])))
    for elem in lista:
        munkalap.append(list(astuple(elem)))


def olvas(tipus, munkafuzet: Workbook, munkalap_nev: str) -> list:
    sorok = munkafuzet[munkalap_nev].iter_rows(values_only=True)
    fejlec = next(sorok)
    return [sorbol_objektum(tipus, dict(zip(fejlec, sor))) for sor in sorok if sor[0] is not None]
