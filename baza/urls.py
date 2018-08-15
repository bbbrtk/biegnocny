from django.urls import path, include
from . import views


urlpatterns = [
    path("start",views.otworz_widok_glowny),

    path("ekipy",views.otworz_ekipy),
    path("ekipa/<int:team_id>", views.otworz_szczegoly_ekipy),

    path("punktyHS",views.otworz_punkty_HS),
    path("punktyW",views.otworz_punkty_W),
    path("punktyR",views.otworz_punkty_R),
    path("punkty/<int:punkt_id>", views.otworz_szczegoly_punktu),

    path("kwadraty",views.otworz_kwadraty),

    #path("pobierz_kopie",views.pobierz_kopie),

    path('', include('django.contrib.auth.urls')),

]
