from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

import xlwt, os, ftplib

from .models import *


"""
def download(filename):
    with ftplib.FTP('94.152.53.137', 'bartek', 'Cervia*5111') as ftp:
        ftp.cwd('/bartoszsobkowiak')
        with open(filename, 'wb') as f:
            ftp.retrbinary('RETR ' + filename, f.write)

"""

def pobierz_kopie(request):
    file_path = '/home/bartoszsobkowiak/biegnocny/kopia_zapasowa.xls'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def eksportuj(arkusz, nazwa, obiekty, lista):
    strona = arkusz.add_sheet(nazwa)
    row = 0
    col = 0
    for atrybut in lista:
        strona.write(row, col, atrybut)
        col += 1

    for obiekt in obiekty:
        col = 0
        row += 1
        for atrybut in lista:
            strona.write(row, col, str(getattr(obiekt,atrybut)))
            col += 1


def eksportuj_wszystko(request):
    arkusz = xlwt.Workbook()

    obiekty = (
        Ekipa.objects.all(), Uczestnik.objects.all(),
        Punkt_HS.objects.all(), Punkt_W.objects.all(),
        Punkt_R.objects.all(), Kwadrat.objects.all(),
        Zgloszenie_HS.objects.all(), Zgloszenie_W.objects.all(),
        Zgloszenie_R.objects.all()
        )

    nazwy = (
        "Ekipy", "Uczestnicy",
        "PunktyHS", "PunktyW",
        "PunktyR", "Kwadraty",
        "ZgloszenieHS", "ZgloszenieW",
        "ZgloszenieR"
        )

    listaEkipa = (
        'lp',
        'id','nazwa','trasa',
        'telefon','zgodnosc_wplat', 'oswiadczenie_patrolowego',
        'obecnosci', 'weryfikacja_zgod', 'pakiet_startowy',
        'do_zaplaty', 'zaplacono', 'pozostalo',
        'zaplacono_na_osobe', 'ile_wege', 'uwagi',
        'test_poczatkowy', 'punkty_za_trase', 'punkty_za_odpowiedzi',
        'punkty_ujemne', 'wynik_koncowy'
        )

    listaUczestnik = (
        'id', '__str__',
        'imie_nazwisko', 'pesel', 'mail',
        'adres', 'obecnosc', 'zgoda_na_udzial',
        'czy_patrolowy', 'uwagi'
        )

    listaPunkt = (
        'id','trasa','numer','kod',
        'nazwa','skrzyzowanie',
        'adres', 'opis_zawieszenia_1', 'opis_zawieszenia_2',
        'opis', 'pytanie', 'odpowiedz',
        'dojscie', 'punktowy', 'uwagi'
        )

    listaKwadrat = (
        'id','nazwa'
        )

    listaZgloszenie = (
        'id', '__str__',
        'podpowiedz', 'zawieszenie', 'brak_punktu',
        'uwagi'
        )

    listy = (
        listaEkipa, listaUczestnik,
        listaPunkt, listaPunkt,
        listaPunkt, listaKwadrat,
        listaZgloszenie, listaZgloszenie,
        listaZgloszenie
        )

    for num in range(len(nazwy)):
        eksportuj(arkusz, nazwy[num], obiekty[num], listy[num])

    arkusz.save("kopia_zapasowa.xls")


def odswiez_widok(request, team_id):
    try:
        weryfikacja_zgod_ekipy = True
        obecnosci_ekipy = True
        ile_osob = 0
        termin_kwota = 0
        punkty_ujemne_suma = 0
        ekipa = Ekipa.objects.get(pk=team_id)

        for i in ekipa.czlonkowie.all():
            ile_osob=ile_osob+1
            if not i.zgoda_na_udzial:
                weryfikacja_zgod_ekipy = False
            if not i.obecnosc:
                obecnosci_ekipy = False

        for i in ekipa.termin_wplat.all():
            termin_kwota = i.kwota

        for i in ekipa.punkty_bieg.all():
            if i.podpowiedz:
                punkty_ujemne_suma += 1
            if i.zawieszenie:
                punkty_ujemne_suma += 2

        Ekipa.objects.filter(pk=team_id).update(ile_osob=ile_osob)
        Ekipa.objects.filter(pk=team_id).update(do_zaplaty=termin_kwota*ile_osob)
        Ekipa.objects.filter(pk=team_id).update(pozostalo=ekipa.do_zaplaty-ekipa.zaplacono)

        if (ekipa.pozostalo==0):
            Ekipa.objects.filter(pk=team_id).update(zgodnosc_wplat=True)
        else:
            Ekipa.objects.filter(pk=team_id).update(zgodnosc_wplat=False)

        Ekipa.objects.filter(pk=team_id).update(obecnosci=obecnosci_ekipy)
        Ekipa.objects.filter(pk=team_id).update(weryfikacja_zgod=weryfikacja_zgod_ekipy)
        Ekipa.objects.filter(pk=team_id).update(punkty_ujemne=punkty_ujemne_suma)

        wynik_koncowy_suma = ekipa.test_poczatkowy+ekipa.punkty_za_trase+ekipa.punkty_za_odpowiedzi-punkty_ujemne_suma
        Ekipa.objects.filter(pk=team_id).update(wynik_koncowy=wynik_koncowy_suma)

        Ekipa.objects.filter(pk=team_id).update(zaplacono_na_osobe=ekipa.zaplacono/ekipa.ile_osob)

    except Ekipa.DoesNotExist:
        raise Http404("Team does not exist")
    return ekipa


@user_passes_test(lambda u: u.has_perm('baza.Ekipy'))
def otworz_ekipy(request):
    iter = 0
    for i in Ekipa.objects.all():
        iter = iter + 1
        Ekipa.objects.filter(pk=i.id).update(lp=iter)
        odswiez_widok(request, i.id)
    context = {
        "Uczestnik":Uczestnik.objects.all(),
        "Ekipy":Ekipa.objects.all()
    }
    return render(request, "baza/ekipy.html", context)


@user_passes_test(lambda u: u.has_perm('baza.WidokGlowny'))
def otworz_widok_glowny(request):
    eksportuj_wszystko(request)
    context = {
    }
    return render(request, "baza/start.html", context)


@user_passes_test(lambda u: u.has_perm('baza.Ekipy'))
def otworz_szczegoly_ekipy(request, team_id):
    ekipa = odswiez_widok(request, team_id)
    context = {
        "ekipa": ekipa,
        "Uczestnik":Uczestnik.objects.all(), # wszyscy uczestnicy
        "ZaliczonyPunkt":ekipa.punkty_bieg.all(),
        "Uczestnicy": ekipa.czlonkowie.all(), # konkretnego zespolu
        "Termin": ekipa.termin_wplat.all(),
        "Kwadrat": ekipa.kwadrat_startowy.all(),
        "PunktStartowy": ekipa.punkt_startowy.all(),
    }
    return render(request, "baza/ekipa_szczegol.html", context)


@user_passes_test(lambda u: u.has_perm('baza.PunktyHS'))
def otworz_punkty_HS(request):
    context = {
        "Punkty":Punkt_HS.objects.all(),
        }
    return render(request, "baza/punkty.html", context)


@user_passes_test(lambda u: u.has_perm('baza.PunktyW'))
def otworz_punkty_W(request):
    context = {
        "Punkty":Punkt_W.objects.all(),
        }
    return render(request, "baza/punkty.html", context)


@user_passes_test(lambda u: u.has_perm('baza.PunktyR'))
def otworz_punkty_R(request):
    context = {
        "Punkty":Punkt_R.objects.all(),
        }
    return render(request, "baza/punkty.html", context)


@user_passes_test(lambda u: u.has_perm('baza.Punkty'))
def otworz_szczegoly_punktu(request, punkt_id):
    try:
        punkt = Punkt.objects.get(pk=punkt_id)
        context = {
        "Punkt": punkt,
        }
    except Ekipa.DoesNotExist:
        raise Http404("Team does not exist")
    return render(request, "baza/punkt_szczegol.html", context)


@user_passes_test(lambda u: u.has_perm('baza.Kwadraty'))
def otworz_kwadraty(request, team_id):
    context = {
        "Kwadraty":Kwadraty.objects.all(),
    }
    return render(request, "baza/kwadraty.html", context)
