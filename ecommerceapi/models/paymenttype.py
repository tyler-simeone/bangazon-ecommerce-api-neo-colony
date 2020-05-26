from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .customer import Customer

class PaymentType(models.Model):
    
    merchant_name = models.CharField(null = False, max_length = 25 )
    account_number = models.CharField(null = False, max_length = 25 )
    expiration_date = models.DateTimeField(null = False)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE )
    created_at = models.DateTimeField(auto_now_add= True)
    
    class Meta:
        verbose_name = ("PaymentType")
        verbose_name_plural = ("PaymentTypes")        
        
    def __str__(self):
        return f"Merchant Name: {self.merchant_name}"
    
    def get_absolute_url(self):
        return reverse("PaymentType_detail", kwargs={"pk": self.pk})