from django.db import models

class Query(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    uf_indicator = models.BooleanField(default=False)
    dolar_indicator = models.BooleanField(default=False)
    tmc_indicator = models.BooleanField(default=False)
	
    def __str__(self):
        return str(self.id)
