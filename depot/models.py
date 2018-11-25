from django.db import models

# Create your models here.
class Depot(models.Model):
    name = models.CharField(max_length=256, help_text=u'仓库名')
    address = models.CharField(max_length=256, help_text=u'地址')
    tel = models.BigIntegerField(help_text=u'联系电话')
    comment = models.TextField(null=True, blank=True, help_text=u'备注')

    class Meta:
        verbose_name = u'仓库'

    def __unicode__(self):
        return self.name