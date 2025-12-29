from django.contrib import admin
from .models import Products, FormulaireContact

admin.site.register(Products)
@admin.register(FormulaireContact)
class FormulaireContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'message', 'date_envoi')
    search_fields = ('nom', 'email', 'message')
    list_filter = ('nom',)


