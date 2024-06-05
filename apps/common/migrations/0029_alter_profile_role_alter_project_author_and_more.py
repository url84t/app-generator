# Generated by Django 4.2.8 on 2024-06-05 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0028_article_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User'), ('COMPANY', 'Company')], default='USER', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='author',
            field=models.ForeignKey(limit_choices_to={'role': 'COMPANY'}, on_delete=django.db.models.deletion.CASCADE, to='common.profile'),
        ),
        migrations.AlterField(
            model_name='team',
            name='author',
            field=models.ForeignKey(limit_choices_to={'role': 'COMPANY'}, on_delete=django.db.models.deletion.CASCADE, related_name='team', to='common.profile'),
        ),
        migrations.AlterField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, limit_choices_to={'role': 'USER'}, related_name='members', to='common.profile'),
        ),
        migrations.AlterField(
            model_name='teamrole',
            name='author',
            field=models.ForeignKey(limit_choices_to={'role': 'USER'}, on_delete=django.db.models.deletion.CASCADE, related_name='team_role', to='common.profile'),
        ),
    ]
