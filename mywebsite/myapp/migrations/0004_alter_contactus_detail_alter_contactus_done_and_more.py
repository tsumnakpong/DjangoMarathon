# Generated by Django 4.2.5 on 2023-09-18 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='รายละเอียด'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='done',
            field=models.BooleanField(default=False, verbose_name='แก้ปัญหาจบแล้วยัง?'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.CharField(max_length=200, verbose_name='อีเมลผู้ติดต่อ'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='name',
            field=models.CharField(max_length=200, verbose_name='ชื่อผู้ถาม'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='summary',
            field=models.TextField(blank=True, null=True, verbose_name='สรุปว่าปัญหานี้แก้อย่างไร'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='title',
            field=models.CharField(max_length=200, verbose_name='ชื่อปัญหา (name)'),
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instock', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('sold', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
            ],
        ),
    ]
