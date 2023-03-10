from django.db import models

# Create your models here.
class product(models.Model):
    product_id= models.AutoField
    product_name=models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    price= models.IntegerField(default=0)
    pub_date= models.DateField()
    image=models.ImageField(upload_to="shop/images", default="")    
    
    def __str__(self):
        return self.product_name
    