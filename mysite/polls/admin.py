from django.contrib import admin

# Register your models here.
from permission import Permission

from polls.models import Transaction
# admin.site.register(Permission)

# admin.site.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id','create_by','reason','start_date','end_date','approve_status']

admin.site.register(Transaction, TransactionAdmin)