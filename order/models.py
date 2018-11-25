from django.db import models
from client.models import Client
from cargo.models import Cargo

TYPE = {
    0: u'买入',
    1: u'卖出'
}
# Create your models here.
class Order(models.Model):
    orderType = models.IntegerField(choices=TYPE, help_text=u'交易类型')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name=u'货物')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name=u'买卖方')
    amount = models.IntegerField(help_text=u'金额')
    restAmount = models.IntegerField(help_text=u'尾款')
    orderTime = models.DateTimeField(help_text=u'日期')
    comment = models.TextField(null=True, blank=True, help_text=u'备注')

    class Meta:
        verbose_name = u'交易'

    def __unicode__(self):
        return self.orderType + '-' + self.cargo.name + '-' + self.client.name
