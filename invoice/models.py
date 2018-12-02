from django.db import models

from order.models import Order

# Create your models here.
class Invoice(models.Model):
    code = models.BigIntegerField(help_text=u'发票号')
    title = models.CharField(max_length=256, help_text=u'发票抬头')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=u'所属订单')
    content = models.CharField(max_length=128, help_text=u'货物名称')
    quantity = models.IntegerField(help_text=u'数量')
    price = models.FloatField(help_text=u'单价（含税）')
    taxfreePrice = models.FloatField(help_text=u'单价（不含税）')
    unit = models.CharField(max_length=8, help_text=u'单位')
    taxRate = models.FloatField(help_text=u'税率')
    cesse = models.FloatField(help_text=u'税额')
    createTime = models.DateTimeField(help_text=u'开票时间')
    sent = models.BooleanField(help_text=u'是否寄出')

    class Meta:
        verbose_name = u'发票'

    def __unicode__(self):
        return self.title