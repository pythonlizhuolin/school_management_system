# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-27 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(blank=True, max_length=20, null=True)),
                ('book_author', models.CharField(blank=True, max_length=20, null=True)),
                ('book_pub', models.CharField(blank=True, max_length=20, null=True)),
                ('book_operator', models.CharField(blank=True, max_length=20, null=True)),
                ('book_put_num', models.CharField(blank=True, max_length=20, null=True)),
                ('book_put_date', models.DateField(auto_now_add=True)),
                ('book_category', models.CharField(blank=True, max_length=20, null=True)),
                ('book_pub_num', models.CharField(blank=True, max_length=20, null=True)),
                ('book_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('book_pub_date', models.DateField(auto_now_add=True)),
                ('book_intro', models.TextField()),
            ],
            options={
                'db_table': 't_book',
            },
        ),
        migrations.CreateModel(
            name='BookBorrow',
            fields=[
                ('borrow_id', models.IntegerField(primary_key=True, serialize=False)),
                ('borrow_time', models.DateField(auto_now_add=True)),
                ('return_time', models.DateField(auto_now_add=True)),
                ('registrar', models.CharField(blank=True, max_length=15, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Book')),
            ],
            options={
                'db_table': 't_book_borrow',
            },
        ),
        migrations.CreateModel(
            name='Clazz',
            fields=[
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cls_name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
            ],
            options={
                'db_table': 't_class',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cour_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('cour_name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 't_course',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('gra_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('gra_name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 't_grade',
            },
        ),
        migrations.CreateModel(
            name='HeadTeacher',
            fields=[
                ('ht_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ht_in_date', models.DateField(auto_now_add=True)),
                ('ht_out_date', models.DateField(auto_now_add=True)),
                ('clazz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.Clazz')),
            ],
            options={
                'db_table': 't_head_teacher',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('maj_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('maj_name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 't_major',
            },
        ),
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('stu_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('stu_gender', models.CharField(blank=True, max_length=2, null=True)),
                ('stu_id_num', models.CharField(blank=True, max_length=20, null=True)),
                ('stu_addr', models.CharField(blank=True, max_length=50, null=True)),
                ('stu_political', models.CharField(blank=True, max_length=10, null=True)),
                ('stu_healthy', models.CharField(blank=True, max_length=10, null=True)),
                ('stu_name', models.CharField(blank=True, max_length=15, null=True)),
                ('stu_age', models.IntegerField(blank=True, null=True)),
                ('stu_birthday', models.DateField(blank=True, null=True)),
                ('stu_phone', models.CharField(blank=True, max_length=11, null=True)),
                ('stu_nation', models.CharField(blank=True, max_length=3, null=True)),
                ('clazz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Clazz')),
            ],
            options={
                'db_table': 't_stu_messenger',
            },
        ),
        migrations.CreateModel(
            name='StuRegister',
            fields=[
                ('sr_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stu_major', models.CharField(blank=True, max_length=12, null=True)),
                ('stu_recommender', models.CharField(blank=True, max_length=10, null=True)),
                ('stu_enrollment', models.DateField(blank=True, null=True)),
                ('stu_score', models.CharField(blank=True, max_length=3, null=True)),
                ('clazz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Clazz')),
                ('stu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.Stu')),
            ],
            options={
                'db_table': 't_stu_register',
            },
        ),
        migrations.CreateModel(
            name='StuScore',
            fields=[
                ('sco_id', models.IntegerField(primary_key=True, serialize=False)),
                ('test_teacher', models.CharField(blank=True, max_length=20, null=True)),
                ('test_date', models.DateField(blank=True, null=True)),
                ('test_category', models.CharField(blank=True, max_length=20, null=True)),
                ('test_score', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
                ('clazz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Clazz')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Course')),
                ('stu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Stu')),
            ],
            options={
                'db_table': 't_stu_score',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tea_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('tea_name', models.CharField(blank=True, max_length=20, null=True)),
                ('tea_gender', models.CharField(blank=True, max_length=3, null=True)),
                ('tea_political', models.CharField(blank=True, max_length=20, null=True)),
                ('tea_edu', models.CharField(blank=True, max_length=20, null=True)),
                ('tea_id_num', models.CharField(blank=True, max_length=20, null=True)),
                ('tea_work_date', models.DateField(blank=True, null=True)),
                ('tea_age', models.IntegerField(blank=True, null=True)),
                ('tea_marry', models.CharField(blank=True, max_length=10, null=True)),
                ('tea_natioin', models.CharField(blank=True, max_length=10, null=True)),
                ('tea_birth', models.DateField(blank=True, null=True)),
                ('tea_phone', models.CharField(blank=True, max_length=11, null=True)),
                ('tea_intro', models.TextField()),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Major')),
            ],
            options={
                'db_table': 't_teacher',
            },
        ),
        migrations.CreateModel(
            name='TeachingStaff',
            fields=[
                ('ts_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tea_in_date', models.DateField(blank=True, null=True)),
                ('tea_out_date', models.DateField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Teacher')),
            ],
            options={
                'db_table': 't_teaching_staff',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('user_password', models.CharField(blank=True, max_length=20, null=True)),
                ('user_nickname', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 't_user',
            },
        ),
        migrations.AddField(
            model_name='headteacher',
            name='teacher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.Teacher'),
        ),
        migrations.AddField(
            model_name='clazz',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Grade'),
        ),
        migrations.AddField(
            model_name='clazz',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Major'),
        ),
        migrations.AddField(
            model_name='bookborrow',
            name='stu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Stu'),
        ),
    ]
