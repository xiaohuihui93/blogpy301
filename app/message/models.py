from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-  # 因代码中使用了中文, 需要加上这一句, 否则报错.
class UserMessage(models.Model):
    object_id = models.CharField(primary_key=True, default="", max_length=100, verbose_name=u"zhujian")
    name = models.CharField(max_length=20, verbose_name=u"user_name")  # verbose_name是作为一个说明字段, 相当于别名.
    email = models.EmailField(verbose_name=u"email")
    address = models.CharField(max_length=100, verbose_name=u"address")
    message = models.CharField(max_length=500, verbose_name=u"comment")

    class Meta:
        verbose_name = u"用户留言信息"
