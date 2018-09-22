from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from . import models

class QueryView(generic.CreateView):
    model = models.Query
    template_name = 'djapi/index.html'
    fields = ('start_date','end_date','uf_indicator','dollar_indicator','tmc_indicator')
    labels = {
        'start_date':'Since',
        'end_date':'To',
        'uf_indicator':'UF',
        'dollar_indicator':'Dollar',
        'tmc_indicator':'TMC',
    }
    
    def get_success_url(self):
        return reverse('djapi:results', args=(self.object.id,))

def results(request, query_id):
    query = get_object_or_404(models.Query, pk=query_id)
    return render(request, 'djapi/results.html', {'query': query})