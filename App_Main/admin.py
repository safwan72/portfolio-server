from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.Projects)
admin.site.register(models.ProjectCategory)
admin.site.register(models.Contact)
admin.site.register(models.NewsLetter)
