
from django.db import models

# #上传图片的模型类
# class Pictures(models.Model):
#     pic = models.ImageField(upload_to='booktest/')
#     def __str__(self):
#         return self.pic
class IMG(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)