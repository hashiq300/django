from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 4


class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [(None, {
  'fields': ['question_text']}),
  ('date information', {'fields': ['pub_date'],'classes':['collapse']}),]
  inlines = [ChoiceInline]


#admin.site.register(Question)
#admin.site.register(Choice)


admin.site.register(Question,QuestionAdmin)