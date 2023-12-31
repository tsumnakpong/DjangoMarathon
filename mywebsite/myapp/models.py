from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ProductStock(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    instock = models.DecimalField(default=1,max_digits=10, decimal_places=2)
    sold = models.DecimalField(default=1,max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product.name +'(instock: {} sold: {})'.format(self.instock,self.sold)

    
class Staff(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ContactUs(models.Model):
    name = models.CharField(max_length=200,verbose_name='ชื่อผู้ถาม')
    title = models.CharField(max_length=200,verbose_name='ชื่อปัญหา (name)')
    detail = models.TextField(null=True,blank=True,verbose_name='รายละเอียด')
    email = models.CharField(max_length=200,verbose_name='อีเมลผู้ติดต่อ')
    done = models.BooleanField(default=False,verbose_name='แก้ปัญหาจบแล้วยัง?')
    summary = models.TextField(null=True,blank=True,verbose_name='สรุปว่าปัญหานี้แก้อย่างไร')

    def __str__(self):
        return self.title