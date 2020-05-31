# Generated by Django 3.0.6 on 2020-05-31 17:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=600)),
            ],
            options={
                'verbose_name': 'Received messages',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village', models.CharField(max_length=30)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egarbage.Cell')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=30)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egarbage.District')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_waste_type', models.CharField(choices=[('Laptop', 'Laptop'), ('Computer', 'Computer'), ('Phone', 'Phone'), ('Radio', 'Radio'), ('Charger', 'Charger'), ('Speaker', 'Speaker'), ('Printer', 'Printer'), ('Headphone', 'Headphone'), ('Cables', 'Cables')], max_length=30)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('street', models.CharField(max_length=50)),
                ('collected', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cells', to='egarbage.Cell')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='districts', to='egarbage.District')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='provinces', to='egarbage.Province')),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sectors', to='egarbage.Sector')),
                ('village', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='egarbage.Village')),
            ],
            options={
                'verbose_name': 'E-Waste',
                'verbose_name_plural': 'E-Waste',
            },
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egarbage.Province'),
        ),
        migrations.AddField(
            model_name='cell',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egarbage.Sector'),
        ),
    ]
