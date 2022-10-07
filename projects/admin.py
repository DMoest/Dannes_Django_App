from django.contrib import admin

from projects.models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'description', 'technology', 'link', 'colaborators')
    list_filter = ('technology', 'colaborators')
    search_fields = ('id', 'title', 'technology', 'colaborators')
