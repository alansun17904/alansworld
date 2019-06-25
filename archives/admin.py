from django.contrib import admin
from .models import PsychologyQuestion, PsychologyStudy


class StudyAdmin(admin.ModelAdmin):
    list_display = ('experimenters', 'year', 'category')
    list_filter = ('experimenters', 'year', 'category')
    search_fields = ('aim', 'method', 'procedure', 'participants', 'results', 'conclusion', 'evaluation')


admin.site.register(PsychologyStudy, StudyAdmin)
admin.site.register(PsychologyQuestion)
