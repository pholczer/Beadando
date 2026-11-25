class Szemely:
    azonosito: str
    nev: str
    orszag: str
    kor: int
    ferfi: bool

    def __init__(self, azonosito: str, nev: str, orszag: str, kor: int, ferfi: bool = True) -> None:
        self.azonosito = azonosito
        self.nev = nev
        self.orszag = orszag
        self.kor = kor
        self.ferfi = ferfi

    def __eq__(self, masik: object) -> bool:
        return isinstance(masik, Szemely) and self.azonosito == masik.azonosito

    def __hash__(self) -> int:
        return self.azonosito.__hash__()

    def __str__(self) -> str:
        return "{0}: {1} ({2}, {3}, {4})".format(self.azonosito, self.nev, self.orszag, self.kor, self.ferfi)


class Csapat:
    azonosito: str
    nev: str
    orszag: str
    kapitany_azonosito: str

    def __init__(self, azonosito: str, nev: str, orszag: str, kapitany_azonosito: str) -> None:
        self.azonosito = azonosito
        self.nev = nev
        self.orszag = orszag
        self.kapitany_azonosito = kapitany_azonosito

    def __eq__(self, masik: object) -> bool:
        return isinstance(masik, Csapat) and self.azonosito == masik.azonosito

    def __hash__(self) -> int:
        return self.azonosito.__hash__()

    def __str__(self) -> str:
        return "{0}: {1} ({2})".format(self.azonosito, self.nev, self.orszag)


class Verseny:
    azonosito: str
    nev: str
    orszag: str
    ev: int
    tav_km: int
    gyoztes_azonosito: str

    def __init__(self, azonosito: str, nev: str, orszag: str, ev: int, tav_km: int,
                 gyoztes_azonosito: str) -> None:
        self.azonosito = azonosito
        self.nev = nev
        self.orszag = orszag
        self.ev = ev
        self.tav_km = tav_km
        self.gyoztes_azonosito = gyoztes_azonosito

    def __eq__(self, masik: object) -> bool:
        return isinstance(masik, Verseny) and self.azonosito == masik.azonosito

    def __hash__(self) -> int:
        return self.azonosito.__hash__()

    def __str__(self) -> str:
        return "{0}: {1} ({2}, {3}, {4} km)".format(self.azonosito, self.nev, self.orszag, self.ev, self.tav_km)
