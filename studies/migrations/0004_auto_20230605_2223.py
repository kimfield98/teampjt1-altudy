# Generated by Django 3.2.18 on 2023-06-05 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0003_alter_study_join_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncementRead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studies.announcement')),
                ('studying', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studies.studying')),
            ],
        ),
        migrations.AddField(
            model_name='announcement',
            name='announcement_read',
            field=models.ManyToManyField(related_name='studying_read', through='studies.AnnouncementRead', to='studies.Studying'),
        ),
    ]