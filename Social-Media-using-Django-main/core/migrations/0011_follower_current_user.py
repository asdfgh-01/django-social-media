# Generated by Django 4.1.4 on 2023-03-21 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_follower_user_following_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='current_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profile'),
        ),
    ]
