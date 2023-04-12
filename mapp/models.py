from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class item(models.Model):
    category=models.ForeignKey(category,related_name="item",on_delete=models.CASCADE)
    iname=models.CharField(max_length=20)
    des=models.TextField(blank=True,null=True)
    price=models.FloatField()
    image=models.FileField(upload_to='item_images',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User,related_name="item",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.iname

