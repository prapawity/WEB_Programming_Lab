# Generated by Django 2.1 on 2019-04-30 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190430_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='approve_status',
            field=models.CharField(choices=[('อนุมัติ', 'อนุมัติ'), ('รอการดำเนินการ', 'รอการดำเนินการ'), ('ไม่อนุมัติ', 'ไม่อนุมัติ')], default='รอการดำเนินการ', max_length=10),
        ),
    ]
