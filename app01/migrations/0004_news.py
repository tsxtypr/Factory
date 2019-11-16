# Generated by Django 2.2.1 on 2019-11-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_product_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=32, verbose_name='技术咨询标题')),
                ('news_desc', models.TextField(verbose_name='咨询描述')),
            ],
            options={
                'db_table': 'news',
            },
        ),
    ]
