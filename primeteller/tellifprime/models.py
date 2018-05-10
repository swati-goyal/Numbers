from django.db import models


class NumValue(models.Model):
    number_value = models.IntegerField(default=0)
    number_property = models.CharField('properties', default='Try another number!', max_length=270)


