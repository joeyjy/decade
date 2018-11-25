from django.db import models
from depot.models import Depot

# Create your models here.
class Cargo(models.Model):
    name = models.CharField(max_length=128, help_text=u'货物名')
    weight = models.IntegerField(help_text=u'重量')
    price = models.IntegerField(help_text=u'单价')
    quantity = models.IntegerField(help_text=u'数量')
    comment = models.TextField(null=True, blank=True, help_text=u'备注')
    depot = models.ForeignKey(Depot, on_delete=models.CASCADE, verbose_name=u'所在仓库')

    class Meta:
        verbose_name = u'货物'

    def __unicode__(self):
        return self.name