from django.contrib import admin
from todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('number', 'text')


admin.site.register(Todo, TodoAdmin)