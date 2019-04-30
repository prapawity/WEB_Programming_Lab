from datetime import date

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from mysite import settings


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    create_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    reason = models.TextField(max_length=2000)
    case1 = 'ลากิจ'
    case2 = 'ลาป่วย'
    Type = (
            (case1,'ลากิจ'),
            (case2, "ลาป่วย"))
    type = models.CharField(max_length=10, choices=Type,default=case1)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    approve = 'อนุมัติ'
    pending = 'รอการดำเนินการ'
    reject = 'ไม่อนุมัติ'
    Approve_status = (
        (approve,"อนุมัติ"),
        (pending, 'รอการดำเนินการ'),
        (reject,'ไม่อนุมัติ'))
    approve_status = models.CharField(max_length=10, choices=Approve_status,default=pending)
