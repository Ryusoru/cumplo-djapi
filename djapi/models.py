from django.db import models
from django.core.exceptions import ValidationError
import datetime

def min_date(date):
    min_date = datetime.date(1990, 1, 1)
    if date < min_date:
        raise ValidationError('Date should be greater than 01/01/1990')
    
def max_date(date):
    max_date = datetime.date.today()
    if date > max_date:
        raise ValidationError('Date should not go beyond today')

class FinantialIndicator(models.Model):
    indicator_name = models.CharField(max_length=256)
	
    def __str__(self):
        return self.indicator_name

class Query(models.Model):
    start_date = models.DateField(validators=[min_date, max_date])
    end_date = models.DateField(validators=[min_date, max_date])
    finantial_indicators = models.ManyToManyField(FinantialIndicator)
    
    def __str__(self):
        name = 'Query-%05d \n' % (self.id)
        return name
