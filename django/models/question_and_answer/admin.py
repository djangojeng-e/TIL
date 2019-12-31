from django.contrib import admin
from .models import Questions, Answers
# Register your models here.

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    pass