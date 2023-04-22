from django.contrib import admin

# Register your models here.
from .models import tasks,Managers,Workers,instructions
admin.site.register(tasks)
admin.site.register(Managers)
admin.site.register(Workers)
admin.site.register(instructions)

