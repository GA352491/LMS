from django.contrib import admin
from Quizapp.models import BaseModel, Questions, Answers, Categories

# Register your models here.
admin.site.register(Categories)
admin.site.register(Questions)
admin.site.register(Answers)
