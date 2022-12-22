from django.db import models

# Create your models here.
class Menu(models.Model):
    nomi = models.CharField(max_length=50)
    def __str__(self):
       return self.nomi
    class Meta:
        verbose_name ="Menu"
        verbose_name_plural ="Menu"

class Maxsulot(models.Model):
    name = models.CharField(max_length=50)
    money = models.IntegerField()
    chegirma_money  = models.IntegerField(null=True,blank=True)
    rasm_link = models.CharField(max_length=100)
    tur = models.ForeignKey(Menu,on_delete=models.CASCADE)
    malumot = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name ="Maxsulot"
        verbose_name_plural ="Maxsulot"

class Message(models.Model):
    user_id = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=500)
    class Meta:
        verbose_name ="Message"
        verbose_name_plural ="Message"