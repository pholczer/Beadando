from dataclasses import dataclass, field, fields


@dataclass
class Szemely:
    azonosito: str = field(hash=True)
    nev: str = field(repr=True, compare=False)
    orszag: str = field(repr=True, compare=False)
    kor: int = field(repr=True, compare=False)
    ferfi: bool = field(default=True, repr=True, compare=False)


@dataclass
class Csapat:
    azonosito: str = field(hash=True)
    nev: str = field(repr=True, compare=False)
    orszag: str = field(repr=True, compare=False)
    kapitany_azonosito: str = field(repr=True, compare=False)


@dataclass
class Verseny:
    azonosito: str = field(hash=True)
    nev: str = field(repr=True, compare=False)
    orszag: str = field(repr=True, compare=False)
    ev: int = field(repr=True, compare=False)
    tav_km: int = field(repr=True, compare=False)
    gyoztes_azonosito: str = field(repr=True, compare=False)


FAJLNEVEK = {Szemely: "szemelyek", Csapat: "csapatok", Verseny: "versenyek"}


def mezonevek(tipus) -> list:
    return [mezo.name for mezo in fields(tipus)]


def sorbol_objektum(tipus, sor: dict):
    ertekek = {}
    for mezo in fields(tipus):
        ertek = sor[mezo.name]
        if mezo.type is bool:
            ertek = str(ertek) == "True"
        else:
            ertek = mezo.type(ertek)
        ertekek[mezo.name] = ertek
    return tipus(**ertekek)
