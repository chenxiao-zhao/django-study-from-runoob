# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.contrib import admin
from TestModel.models import Test,Contact,Tag
# Register your models here.
class TagInline(admin.TabularInline):
    model =Tag

class ContactAdmin(admin.ModelAdmin):
    list_display =('name','age','email')
    search_fields = ('name',)
    inlines = [TagInline]
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes':('collapse',),
            'fields':('age',),
        }]
    )

admin.site.register(Contact,ContactAdmin)
admin.site.register([Test])
