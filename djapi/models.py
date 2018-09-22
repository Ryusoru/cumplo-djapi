from django.db import models

class Query(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    uf_indicator = models.BooleanField(default=False)
    dollar_indicator = models.BooleanField(default=False)
    tmc_indicator = models.BooleanField(default=False)
	
    def __str__(self):
        name = 'Query-%05d \n' % (self.id)
        return name
