# Create your models here.
from django.db import models

class Product(models.Model):
    #产品名称
    product_name=models.CharField(max_length=20,verbose_name='产品名称')
    #产品描述
    product_desc=models.TextField(verbose_name='产品描述')
    #用途
    product_use=models.CharField(max_length=32,verbose_name='产品用途')
    picture=models.ImageField(upload_to='images')

    def __str__(self):
        return self.product_name

    class Meta:
        db_table='product'

class News(models.Model):
    news_title=models.CharField(max_length=32,verbose_name="技术咨询标题")
    news_desc=models.TextField(verbose_name="咨询描述")
    news_time=models.DateField(auto_now=True,verbose_name="文章的时间")

    def __str__(self):
        return self.news_title

    class Meta:
        db_table='news'