from django.urls import path, include
from . import views


urlpatterns = [
    path("start",views.otworz_widok_glowny),

    path("ekipy",views.otworz_ekipy),
    path("ekipyHS", views.otworz_ekipy_HS),
    path("ekipyW", views.otworz_ekipy_W),
    path("ekipyR", views.otworz_ekipy_R),
    path("ekipa/<int:team_id>", views.otworz_szczegoly_ekipy),

    path("punktyHS",views.otworz_punkty_HS),
    path("punktyW",views.otworz_punkty_W),
    path("punktyR",views.otworz_punkty_R),
    path("punkty/<int:punkt_id>", views.otworz_szczegoly_punktu),

    path("kwadraty",views.otworz_kwadraty),
    path("instrukcje",views.otworz_instrukcje),
    path("ustawienia",views.otworz_ustawienia),

    #path("pobierz_kopie",views.pobierz_kopie),
    #path("pobierz_kopie/<str:trasa>",views.pobierz_punkty),
    path('', include('django.contrib.auth.urls')),

]
