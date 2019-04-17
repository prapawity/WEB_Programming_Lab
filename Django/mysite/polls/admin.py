from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission
from polls.models import Poll,Question,Choice
admin.register(Permission)

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class ChoiceInline(admin.TabularInline):
    model = Choice

class PollAdmin(admin.ModelAdmin):
    list_display = ['id','title','start_date','end_date','del_flag']
    list_per_page = 15
    list_filter = ['start_date','end_date','del_flag']
    search_fields = ['title']
    fieldsets = [(None,{'fields': ['title','del_flag']}),('Active Durations', {'fields':['start_date','end_date'],'classes': ['collapes']})]
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','poll','text']
    list_per_page = 15

    inlines = [ChoiceInline]





class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id','question','text','value']

admin.site.register(Poll,PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)

