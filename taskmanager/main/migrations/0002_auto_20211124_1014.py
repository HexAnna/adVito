# Generated by Django 3.2.9 on 2021-11-24 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advert',
            options={'verbose_name': 'Обьявление', 'verbose_name_plural': 'Обьявления'},
        ),
        migrations.AddField(
            model_name='advert',
            name='date_edit',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='advert',
            name='date_pub',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='advert',
            name='img',
            field=models.ImageField(default=1, upload_to=main.models.user_avatar_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advert',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='user_likes_it', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to=main.models.user_avatar_path)),
                ('my_adverts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_adverts', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='advert',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
        ),
    ]