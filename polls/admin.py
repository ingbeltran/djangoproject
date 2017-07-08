# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Choice, Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('question_text', 'pub_date')
    search_fields = ('question_text', 'pub_date')
    #list_editable = ('question_text', 'pub_date')
    #actions = [export_as_csv]
    

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes')
    list_filter = ('choice_text', 'votes')
    search_fields = ('choice_text', 'votes')
    raw_id_fields = ('question',)

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Choice,ChoiceAdmin)