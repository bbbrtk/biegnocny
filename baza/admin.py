from django.contrib import admin
from .models import *


admin.site.register(Profile)
admin.site.register(Uczestnik)

admin.site.register(Ekipa)
admin.site.register(Ekipa_HS)
admin.site.register(Ekipa_W)
admin.site.register(Ekipa_R)

admin.site.register(Kwadrat)
admin.site.register(Termin)

admin.site.register(Punkt)
admin.site.register(Punkt_HS)
admin.site.register(Punkt_W)
admin.site.register(Punkt_R)

admin.site.register(Zgloszenie_HS)
admin.site.register(Zgloszenie_W)
admin.site.register(Zgloszenie_R)
