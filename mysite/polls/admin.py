from django.contrib import admin

# Register your models here.
from permission import Permission

from polls.models import Transaction
# admin.site.register(Permission)

# admin.site.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id','create_by','reason','start_date','end_date','approve_status']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['create_by', 'reason', 'type', 'start_date', 'end_date', ]
        else:
            return ['approve_status', ]

admin.site.register(Transaction, TransactionAdmin)