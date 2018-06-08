from django.contrib import admin
from .models import Course

class CoursesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    list_search = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Course, CoursesAdmin)

