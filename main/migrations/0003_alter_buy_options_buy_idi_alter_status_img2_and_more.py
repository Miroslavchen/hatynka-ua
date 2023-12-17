# Generated by Django 4.2.1 on 2023-11-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_buy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buy',
            options={'verbose_name': 'Покупку', 'verbose_name_plural': 'Покупки'},
        ),
        migrations.AddField(
            model_name='buy',
            name='idi',
            field=models.CharField(db_index=True, default=1, max_length=1000000, unique=False, verbose_name='id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='status',
            name='Img2',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Img2'),
        ),
        migrations.AlterField(
            model_name='status',
            name='Img3',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Img3'),
        ),
        migrations.AlterField(
            model_name='status',
            name='Img4',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Img4'),
        ),
    ]
