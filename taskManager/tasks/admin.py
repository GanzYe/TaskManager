from django.contrib import admin
from tasks.models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at')
    list_filter = ('title', 'author', 'status', 'created_at')
    search_fields = ['title']
