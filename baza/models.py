from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Punkt (models.Model):
    id =  models.AutoField(primary_key=True)
    numer = models.IntegerField(default=0)
    kod = models.CharField(max_length=3, blank=True)

    nazwa = models.CharField(max_length=128, blank=True)
    skrzyzowanie = models.CharField(max_length=128, blank=True)
    adres = models.CharField(max_length=128, blank=True)

    opis_zawieszenia_1 = models.CharField(max_length=256, blank=True)
    opis_zawieszenia_2 = models.CharField(max_length=256, blank=True)
    opis = models.CharField(max_length=1024, blank=True)
    pytanie = models.CharField(max_length=256, blank=True)
    odpowiedz = models.CharField(max_length=256, blank=True)
    dojscie = models.CharField(max_length=256, blank=True)
    foto = models.ImageField(blank=True, upload_to='baza/static/foto/', default='baza/static/foto/{self.id}.jpg')

    punktowy = models.CharField(max_length=64, blank=True)
    uwagi = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f"p_{self.numer} ({self.nazwa})"

    class Meta:
        ordering = ('numer',)

class Punkt_HS (Punkt):
    trasa =  models.CharField(max_length=2, default='HS', blank=True)

class Punkt_W (Punkt):
    trasa =  models.CharField(max_length=2, default='W', blank=True)

class Punkt_R (Punkt):
    trasa =  models.CharField(max_length=2, default='R', blank=True)


class Zgloszenie (models.Model):
    id =  models.AutoField(primary_key=True)
    podpowiedz = models.BooleanField(default=False)
    zawieszenie = models.BooleanField(default=False)
    brak_punktu = models.BooleanField(default=False)
    uwagi = models.CharField(max_length=256, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        nazwa=""
        for i in self.ekipa_set.all():
            nazwa = i.nazwa
        return f"z_{self.punkt}_{self.id}_{nazwa}"

class Zgloszenie_HS (Zgloszenie):
    punkt = models.ForeignKey(Punkt_HS, on_delete=models.CASCADE )

class Zgloszenie_W (Zgloszenie):
    punkt = models.ForeignKey(Punkt_W, on_delete=models.CASCADE )

class Zgloszenie_R (Zgloszenie):
    punkt = models.ForeignKey(Punkt_R, on_delete=models.CASCADE )



class Termin (models.Model):
    id =  models.AutoField(primary_key=True)
    termin = models.CharField(max_length=64)
    kwota = models.FloatField(default=0)

    def __str__(self):
        return f"{self.kwota}zł - {self.termin}"

    class Meta:
        ordering = ('id',)


class Kwadrat (models.Model):
    nazwa = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nazwa}"

    class Meta:
        ordering = ('nazwa',)


class Uczestnik(models.Model):
    imie_nazwisko = models.CharField(max_length=64)
    id =  models.AutoField(primary_key=True)
    pesel = models.CharField(max_length=64)
    mail = models.EmailField(max_length=64)
    adres = models.CharField(max_length=64)
    czy_patrolowy = models.BooleanField(default=False)
    obecnosc = models.BooleanField(default=False)
    zgoda_na_udzial = models.BooleanField(default=False)
    uwagi = models.CharField(max_length=256, default="", blank=True)

    def __str__(self):
        nazwa=""
        for i in self.ekipa_set.all():
            nazwa = i.nazwa
        return f"{self.imie_nazwisko} [{nazwa}] "

    class Meta:
        ordering = ('imie_nazwisko',)


class Ekipa(models.Model):
    TRASY = (
        ('HS', 'Starszoharcerska'),
        ('W', 'Wedrownicza'),
        ('R', 'Rowerowa'),)
    PUNKTY = (
        (Punkt_W, 'P Wedrownicza'),
        (Punkt_R, 'P Rowerowa'),)

    # podstawowe informacje
    nazwa =  models.CharField(max_length=64,default='')
    id =  models.AutoField(primary_key=True)
    trasa =  models.CharField(max_length=2, choices=TRASY, default='HS')
    telefon =  models.CharField(max_length=64, default='')
    zaplacono = models.FloatField(default=0)
    termin_wplat = models.ManyToManyField(Termin)
    # czlonkowie
    czlonkowie = models.ManyToManyField(Uczestnik)
    ile_osob = models.IntegerField(default=0)
    # finanse
    lp = models.IntegerField(default=0)
    do_zaplaty = models.FloatField(default=0)
    zaplacono_na_osobe = models.FloatField(default=0)
    pozostalo = models.FloatField(default=0)
    zgodnosc_wplat = models.BooleanField(default=False)
    # dokumenty
    oswiadczenie_patrolowego = models.BooleanField(default=False)
    obecnosci = models.BooleanField(default=False)
    weryfikacja_zgod = models.BooleanField(default=False)
    pakiet_startowy = models.BooleanField(default=False)
    # inne
    ile_wege = models.IntegerField(default=0)
    uwagi = models.CharField(max_length=256, default="", blank=True)
    # biegowe
    kwadrat_startowy = models.ManyToManyField(Kwadrat, blank=True)
    punkt_startowy = models.ManyToManyField(Punkt_HS, blank=True)
    punkty_bieg = models.ManyToManyField(Zgloszenie_HS, blank=True)
    #
    # punkty
    test_poczatkowy = models.IntegerField(default=0)
    punkty_za_trase = models.IntegerField(default=0)
    punkty_za_odpowiedzi = models.IntegerField(default=0)
    punkty_ujemne = models.IntegerField(default=0)
    wynik_koncowy = models.IntegerField(default=0)

    def __str__(self):
        return f"[{self.trasa}{self.id}] {self.nazwa}"

    class Meta:
        ordering = ('id',)


class Ekipa_HS (Ekipa):
    trasy =  models.CharField(max_length=2, default='HS', blank=True)

class Ekipa_W (Ekipa):
    trasy =  models.CharField(max_length=2, default='W', blank=True)

class Ekipa_R (Ekipa):
    trasy =  models.CharField(max_length=2, default='R', blank=True)


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    class Meta:
        permissions = (
            ('WidokGlowny', 'Strona Główna'),

            ('Punkty', 'Wszystkie punkty'),
            ('PunktyHS', 'HS punkty'),
            ('PunktyW', 'W punkty '),
            ('PunktyR', 'R punkty '),

            ('Kwadraty', 'Kwadraty'),

            ('Ekipy', 'Wszystkie ekipy '),
            ('EkipyHS', 'HS ekipy '),
            ('EkipyW', 'W ekipy '),
            ('EkipyR', 'R ekipy'),

            ('Uczestnicy', 'Wyświetlanie uczestników'),
        )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
"""
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""
