from django.contrib import admin
from Quizapp.models import BaseModel, Questions, Answers, Categories

# Register your models here.
admin.site.register(Categories)


class AnswerAdmin(admin.StackedInline):
    model = Answers


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


# admin.site.register(Questions)
admin.site.register(Answers)
