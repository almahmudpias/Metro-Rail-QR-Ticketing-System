# Generated by Django 3.2.9 on 2021-12-14 16:27

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_guser', models.BooleanField(default=False)),
                ('is_trainmaster', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=30)),
                ('dest', models.CharField(max_length=30)),
                ('routeid', models.IntegerField()),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status', models.CharField(choices=[('Booked', 'Booked'), ('Cancelled', 'Cancelled'), ('Confirmed', 'Confirmed')], default='Booked', max_length=15)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Not_Paid', 'Not_Paid'), ('Refunded', 'Refunded')], default='Not_Paid', max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('routeId', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=200)),
                ('dest', models.CharField(max_length=200)),
                ('nos', models.DecimalField(decimal_places=0, max_digits=2)),
                ('rem', models.DecimalField(decimal_places=0, max_digits=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GeneralUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TrainMaster',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('location', models.CharField(max_length=500)),
                ('licenseNumber', models.CharField(max_length=200)),
            ],
        ),
    ]