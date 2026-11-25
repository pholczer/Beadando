import random

from faker import Faker

from data.alap.modell_adatosztalyok import Szemely, Csapat, Verseny

ORSZAGOK = {
    "Magyarország": ("hu_HU", "{} Nagydíj"),
    "Franciaország": ("fr_FR", "Tour de {}"),
    "Olaszország": ("it_IT", "Giro di {}"),
    "Spanyolország": ("es_ES", "Vuelta a {}"),
    "Németország": ("de_DE", "{} Rundfahrt"),
    "Hollandia": ("nl_NL", "Ronde van {}"),
    "Dánia": ("da_DK", "{} Rundt"),
    "Lengyelország": ("pl_PL", "Memoriał {}"),
    "Egyesült Királyság": ("en_GB", "Tour of {}"),
    "Egyesült Államok": ("en_US", "Tour of {}"),
    "Portugália": ("pt_PT", "Volta a {}"),
    "Csehország": ("cs_CZ", "Okolo {}"),
    "Szlovénia": ("sl_SI", "Velika nagrada {}"),
    "Ausztrália": ("en_AU", "Tour of {}"),
}

CSAPAT_NEV_MINTAK = ["Team {}", "{} Racing", "{} Cycling Team"]


def fakerek_keszitese(orszagok: dict) -> dict:
    return {orszag: Faker(adatok[0]) for orszag, adatok in orszagok.items()}


def szemelyek_generalasa(darab: int, ferfi_arany: float = 0.8, orszagok: dict = ORSZAGOK,
                         egyedi: bool = True, min_kor: int = 18, max_kor: int = 40) -> list[Szemely]:
    assert darab > 0
    assert 0 < ferfi_arany < 1
    assert len(orszagok) > 0
    assert 0 <= min_kor <= max_kor

    fakerek = fakerek_keszitese(orszagok)
    szemelyek = []
    for i in range(darab):
        orszag = random.choice(list(orszagok))
        faker = fakerek[orszag]
        generator = faker.unique if egyedi else faker
        ferfi = random.random() < ferfi_arany
        szemelyek.append(Szemely(
            "SZ-" + str(i + 1).zfill(4),
            generator.name_male() if ferfi else generator.name_female(),
            orszag,
            random.randint(min_kor, max_kor),
            ferfi))
    return szemelyek


def csapatok_generalasa(darab: int, szemelyek: list[Szemely], orszagok: dict = ORSZAGOK,
                        egyedi: bool = True) -> list[Csapat]:
    assert darab > 0
    assert len(szemelyek) > 0 and len(orszagok) > 0

    fakerek = fakerek_keszitese(orszagok)
    csapatok = []
    for i in range(darab):
        orszag = random.choice(list(orszagok))
        faker = fakerek[orszag]
        generator = faker.unique if egyedi else faker
        hazai = [szemely for szemely in szemelyek if szemely.orszag == orszag]
        csapatok.append(Csapat(
            "CS-" + str(i + 1).zfill(4),
            random.choice(CSAPAT_NEV_MINTAK).format(generator.last_name()),
            orszag,
            random.choice(hazai if hazai else szemelyek).azonosito))
    return csapatok


def versenyek_generalasa(darab: int, szemelyek: list[Szemely], orszagok: dict = ORSZAGOK,
                         egyedi: bool = False, min_ev: int = 2015, max_ev: int = 2025,
                         min_tav_km: int = 80, max_tav_km: int = 220) -> list[Verseny]:
    assert darab > 0
    assert len(szemelyek) > 0 and len(orszagok) > 0
    assert min_ev <= max_ev
    assert 0 < min_tav_km <= max_tav_km

    fakerek = fakerek_keszitese(orszagok)
    versenyek = []
    for i in range(darab):
        orszag = random.choice(list(orszagok))
        faker = fakerek[orszag]
        generator = faker.unique if egyedi else faker
        minta = orszagok[orszag][1]
        versenyek.append(Verseny(
            "V-" + str(i + 1).zfill(4),
            minta.format(generator.city()),
            orszag,
            random.randint(min_ev, max_ev),
            random.randint(min_tav_km, max_tav_km),
            random.choice(szemelyek).azonosito))
    return versenyek


def adathalmaz_generalasa(darab: int):
    assert darab > 0

    szemelyek = szemelyek_generalasa(darab)
    csapatok = csapatok_generalasa(max(2, darab // 5), szemelyek)
    versenyek = versenyek_generalasa(max(3, darab // 4), szemelyek)
    return szemelyek, csapatok, versenyek
