from django.db import models

# Create your models here.
class Invoice(models.Model):
    code = models.BigIntegerField(help_text=u'发票号')
    title = models.CharField(max_length=256, help_text=u'发票抬头')
    