# Generated by Django 5.1.5 on 2025-04-05 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_student_volunteer_alter_blog_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.BooleanField(default=1),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='content.student')),
            ],
            options={
                'unique_together': {('student', 'date')},
            },
        ),
    ]
