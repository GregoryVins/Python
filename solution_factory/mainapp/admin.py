from django.contrib import admin

# Register your models here.
from mainapp.models import Polling, Question, Answer

admin.site.register(Polling)
admin.site.register(Question)
admin.site.register(Answer)
