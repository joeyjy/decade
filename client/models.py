from django.db import models

GENDER = (
    (0, u'女'),
    (1, u'男')
)


class Company(models.Model):
    name = models.CharField(max_length=256, help_text=u'公司名')
    address = models.CharField(max_length=256, help_text=u'地址')
    tel = models.BigIntegerField(help_text=u'联系电话')
    comment = models.TextField(null=True, blank=True, help_text=u'备注')

    class Meta:
        verbose_name = u'公司'

    def __unicode__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=256, help_text=u'客户名')
    gender = models.IntegerField(choices=GENDER)
    tel = models.BigIntegerField(help_text=u'联系电话')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=u'所属公司')

    class Meta:
        verbose_name = u'客户'

    def __unicode__(self):
        return self.name