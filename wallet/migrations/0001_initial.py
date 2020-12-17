# Generated by Django 3.1.4 on 2020-12-17 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YourPocket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(editable=False)),
                ('active', models.BooleanField(default=True)),
                ('balance', models.FloatField(default=0)),
                ('expiry_date', models.DateTimeField(editable=False)),
                ('your_pocket_information', models.JSONField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(editable=False)),
                ('is_block', models.BooleanField(default=False)),
                ('pocket_name', models.CharField(editable=False, max_length=128)),
                ('balance', models.FloatField(default=0)),
            ],
            options={
                'unique_together': {('pocket_name', 'user_id')},
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(editable=False)),
                ('amount', models.FloatField(editable=False)),
                ('transaction_information', models.JSONField(editable=False)),
                ('wallet_type', models.CharField(choices=[('w', 'Wallet'), ('y', 'Your Pocket')], default='w', editable=False, max_length=1)),
                ('wallet', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.wallet')),
                ('your_pocket', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='wallet.yourpocket')),
            ],
        ),
    ]