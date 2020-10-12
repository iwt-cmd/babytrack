from django.contrib import admin
from .models import BabyTrack

class BabyTrackAdmin(admin.ModelAdmin):
    list_display=('name', 'date', 'wet', 'dirty', 'leftside', 'rightside', 'sup_amount', 'sup_f', 'sup_b')
    list_display_links=('name', 'date')


admin.site.register(BabyTrack, BabyTrackAdmin)