from django.db import models
from company.models import Company

GENDER = {
    0: u'女',
    1: u'男'
}
# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=256, help_text=u'客户名')
    gender = models.IntegerField(choices=GENDER)
    tel = models.BigIntegerField(help_text=u'联系电话')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=u'所属公司')

    class Meta:
        verbose_name = u'客户'

    def __unicode__(self):
        return self.name