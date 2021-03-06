# Generated by Django 3.2.8 on 2021-11-18 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import margins.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_head', models.BooleanField(default=False)),
                ('is_supervisor', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', margins.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('date', models.DateField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('user_policy', models.CharField(max_length=80, null=True)),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('morpho_device', models.CharField(max_length=80)),
                ('key', models.CharField(max_length=50)),
                ('access', models.CharField(max_length=50)),
                ('department', models.CharField(blank=True, max_length=80, null=True)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('timein', models.CharField(blank=True, max_length=80, null=True)),
                ('timeout', models.CharField(blank=True, max_length=80, null=True)),
                ('regular', models.CharField(blank=True, max_length=20, null=True)),
                ('ot', models.CharField(blank=True, max_length=20, null=True)),
                ('total', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=60, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('user_policy', models.CharField(max_length=80)),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('department', models.CharField(max_length=80)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('timein', models.CharField(blank=True, max_length=80, null=True)),
                ('timeout', models.CharField(blank=True, max_length=80, null=True)),
                ('regular', models.CharField(blank=True, max_length=20, null=True)),
                ('ot', models.CharField(blank=True, max_length=20, null=True)),
                ('total', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ICPSAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('user_policy', models.CharField(blank=True, max_length=80, null=True)),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('morpho_device', models.CharField(max_length=80)),
                ('key', models.CharField(max_length=50)),
                ('access', models.CharField(max_length=50)),
                ('department', models.CharField(blank=True, max_length=80, null=True)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('timein', models.CharField(blank=True, max_length=80, null=True)),
                ('timeout', models.CharField(blank=True, max_length=80, null=True)),
                ('regular', models.CharField(blank=True, max_length=20, null=True)),
                ('ot', models.CharField(blank=True, max_length=20, null=True)),
                ('total', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ICPSEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True, unique=True)),
                ('user_policy', models.CharField(max_length=80)),
                ('employee_id', models.IntegerField(blank=True, null=True)),
                ('department', models.CharField(max_length=80)),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('timein', models.CharField(blank=True, max_length=80, null=True)),
                ('timeout', models.CharField(blank=True, max_length=80, null=True)),
                ('regular', models.CharField(blank=True, max_length=20, null=True)),
                ('ot', models.CharField(blank=True, max_length=20, null=True)),
                ('total', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
