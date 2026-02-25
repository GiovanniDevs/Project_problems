from django.contrib import admin
from .models import Problem, Take
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Problem)
class ProblemsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_date')
    search_fields = ['title', 'description']
    list_filter = ('status', 'created_date',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


admin.site.register(Take)
