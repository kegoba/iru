# Generated by Django 2.2.3 on 2019-11-27 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=100, verbose_name='password')),
                ('phone', models.CharField(max_length=15, null=True, verbose_name='phone number')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date join')),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0, null=True, verbose_name='number of likes')),
                ('shares', models.IntegerField(default=0, null=True, verbose_name='number of shares')),
                ('quote', models.IntegerField(default=0, null=True, verbose_name='number of quote')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_share', to='blog.User')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tittle', models.CharField(blank=True, max_length=255, verbose_name='tittle of post')),
                ('post_body', models.CharField(blank=True, max_length=25555, verbose_name='post')),
                ('post_by', models.CharField(blank=True, max_length=255, verbose_name='author name')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='time posted')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to='blog.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=2555, null=True, verbose_name='comment')),
                ('comment_by', models.CharField(max_length=255, null=True, verbose_name='Last name')),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='time commented')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to='blog.User')),
            ],
        ),
    ]
